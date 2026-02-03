"""HTTP client for OpenAPI: base URL from env, auth from core.auth, timeouts and error handling."""

import json
import os
from typing import Any

import requests

from core.auth import get_auth_headers


def get_base_url() -> str:
    """Base URL from env or default."""
    url = os.environ.get("OPENAPI_BASE_URL", "").strip()
    if not url:
        raise ValueError(
            "Missing OPENAPI_BASE_URL. Set it in .env (e.g. the OpenAPI servers[0].url value)."
        )
    return url.rstrip("/")


def call(
    path: str,
    method: str,
    path_params: dict[str, Any] | None = None,
    query_params: dict[str, Any] | None = None,
    body: Any = None,
) -> dict[str, Any]:
    """
    Call the API: path (with path_params substituted), method, optional query and body.
    Returns parsed JSON or {"error": "..."}. Never raises; errors are returned as dict.
    """
    path_params = path_params or {}
    query_params = query_params or {}
    base = get_base_url()
    url_path = path
    for k, v in path_params.items():
        url_path = url_path.replace("{" + k + "}", str(v))
    url = f"{base}{url_path}"
    headers = get_auth_headers()
    headers.setdefault("Content-Type", "application/json")
    timeout = 30
    try:
        if method.upper() == "GET":
            r = requests.get(url, params=query_params, headers=headers, timeout=timeout)
        elif method.upper() == "POST":
            r = requests.post(url, params=query_params, json=body, headers=headers, timeout=timeout)
        elif method.upper() == "PUT":
            r = requests.put(url, params=query_params, json=body, headers=headers, timeout=timeout)
        elif method.upper() == "PATCH":
            r = requests.patch(url, params=query_params, json=body, headers=headers, timeout=timeout)
        elif method.upper() == "DELETE":
            r = requests.delete(url, params=query_params, headers=headers, timeout=timeout)
        else:
            return {"error": f"Unsupported method: {method}"}
        r.raise_for_status()
        if not r.text.strip():
            return {}
        return r.json()
    except requests.RequestException as e:
        msg = str(e)
        if hasattr(e, "response") and e.response is not None and e.response.text:
            try:
                err_body = e.response.json()
                msg = err_body.get("message", err_body.get("error", e.response.text))[:500]
            except Exception:
                msg = e.response.text[:500]
        return {"error": msg, "isError": True}
    except (ValueError, json.JSONDecodeError) as e:
        return {"error": str(e)[:500], "isError": True}

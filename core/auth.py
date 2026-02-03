"""Authentication: read token from env and return headers for API requests."""

import os


def get_auth_headers() -> dict[str, str]:
    """Return Authorization header from env. Raises if token not set."""
    token = os.environ.get("API_ACCESS_TOKEN")
    if not token or not token.strip():
        raise ValueError(
            "Missing API_ACCESS_TOKEN. Set it in .env or environment (e.g. export API_ACCESS_TOKEN=your_token)."
        )
    return {"Authorization": f"Bearer {token.strip()}"}

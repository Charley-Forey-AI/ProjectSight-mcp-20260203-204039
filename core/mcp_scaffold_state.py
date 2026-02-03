"""Holds spec and selected endpoints for resource handlers (read-only). Reads from JSON in this dir."""

import json
from pathlib import Path

_SPEC = None
_SELECTED = None

def _data_dir():
    return Path(__file__).resolve().parent

def get_spec():
    global _SPEC
    if _SPEC is None:
        p = _data_dir() / "openapi_spec.json"
        if p.exists():
            with open(p, encoding="utf-8") as f:
                _SPEC = json.load(f)
        else:
            _SPEC = {}
    return _SPEC

def get_selected_endpoints():
    global _SELECTED
    if _SELECTED is None:
        p = _data_dir() / "selected_endpoints.json"
        if p.exists():
            with open(p, encoding="utf-8") as f:
                _SELECTED = json.load(f)
        else:
            _SELECTED = []
    return _SELECTED

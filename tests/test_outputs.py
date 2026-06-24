import json
from pathlib import Path

REPORT = Path("/app/report.json")

# Expected values computed from the fixed /app/access.log (6 lines):
#   /index.html x3, /about.html x2, /api/login x1
#   IPs: 192.168.0.1, 192.168.0.2, 10.0.0.5
EXPECTED_TOTAL_REQUESTS = 6
EXPECTED_UNIQUE_IPS = 3
EXPECTED_TOP_PATH = "/index.html"


def _load():
    return json.loads(REPORT.read_text())


def test_report_exists():
    """Success criterion 1: a file exists at /app/report.json."""
    assert REPORT.exists(), "no /app/report.json was produced"


def test_report_is_valid_json_object():
    """Success criterion 2: report.json contains valid JSON (a single object)."""
    report = _load()
    assert isinstance(report, dict), "report.json must be a single JSON object"


def test_total_requests():
    """Success criterion 3: total_requests equals the number of non-empty lines."""
    assert _load().get("total_requests") == EXPECTED_TOTAL_REQUESTS


def test_unique_ips():
    """Success criterion 4: unique_ips equals the distinct client IP count."""
    assert _load().get("unique_ips") == EXPECTED_UNIQUE_IPS


def test_top_path():
    """Success criterion 5: top_path equals the most frequently requested path."""
    assert _load().get("top_path") == EXPECTED_TOP_PATH

import pytest
from reader import read_logs

def test_read_logs_valid(tmp_path):
    file = tmp_path / "test.json"
    file.write_text('{"@timestamp": "2025-08-01", "url": "/test", "duration": 100}\n')
    logs = read_logs([str(file)])
    assert len(logs) == 1

def test_read_logs_with_invalid_json(tmp_path):
    file = tmp_path / "test.json"
    file.write_text('invalid_json\n{"@timestamp": "2025-08-01", "url": "/test", "duration": 100}\n')
    logs = read_logs([str(file)])
    assert len(logs) == 1

def test_read_logs_with_date_filter(tmp_path):
    file = tmp_path / "test.json"
    file.write_text(
        '{"@timestamp": "2025-08-01", "url": "/test", "duration": 100}\n'
        '{"@timestamp": "2025-07-30", "url": "/test", "duration": 200}\n'
    )
    logs = read_logs([str(file)], date_filter="2025-08-01")
    assert len(logs) == 1

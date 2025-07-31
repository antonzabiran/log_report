import pytest
from log_report.reader import read_logs
import tempfile
import json

def test_read_logs_valid():
    # Создаем временный лог-файл
    data = {"endpoint": "/api/test", "response_time": 123}
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
        tmp.write(json.dumps(data) + "\n")
        tmp.seek(0)
        result = read_logs([tmp.name])

    assert isinstance(result, list)
    assert result[0]["endpoint"] == "/api/test"


def test_read_logs_with_invalid_line():
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
        tmp.write("this is not json\n")
        tmp.write(json.dumps({"endpoint": "/api/ok", "response_time": 200}))
        tmp.seek(0)
        result = read_logs([tmp.name])

    assert len(result) == 1
    assert result[0]["endpoint"] == "/api/ok"
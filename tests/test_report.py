from log_report.report import generate_average_report

def test_generate_average_report():
    logs = [
        {"endpoint": "/api/test", "response_time": 100},
        {"endpoint": "/api/test", "response_time": 200},
        {"endpoint": "/api/other", "response_time": 50}
    ]
    report = generate_average_report(logs)

    assert any(row[0] == "/api/test" and row[1] == 2 and row[2] == 150.0 for row in report)
    assert any(row[0] == "/api/other" and row[1] == 1 and row[2] == 50.0 for row in report)

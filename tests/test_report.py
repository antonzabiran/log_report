from report import generate_average_report

def test_generate_average_report():
    logs = [
        {"url": "/home", "duration": 100},
        {"url": "/home", "duration": 200},
        {"url": "/about", "duration": 50},
    ]
    report = generate_average_report(logs)
    assert len(report) == 2
    for row in report:
        assert "url" in row and "average_duration" in row

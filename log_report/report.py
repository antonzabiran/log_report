from collections import defaultdict

def generate_average_report(logs):
    endpoint_data = defaultdict(lambda: {"count": 0, "total_time": 0})

    for entry in logs:
        endpoint = entry.get("endpoint")
        response_time = entry.get("response_time")

        if endpoint and isinstance(response_time, (int, float)):
            endpoint_data[endpoint]["count"] += 1
            endpoint_data[endpoint]["total_time"] += response_time

    report = []
    for endpoint, data in endpoint_data.items():
        avg_time = round(data["total_time"] / data["count"], 2)
        report.append([endpoint, data["count"], avg_time])

    return report

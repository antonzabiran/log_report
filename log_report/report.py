from collections import defaultdict

def generate_average_report(logs):
    durations = defaultdict(list)
    for log in logs:
        endpoint = log.get("url")
        duration = log.get("duration")
        if endpoint and isinstance(duration, (int, float)):
            durations[endpoint].append(duration)

    table = []
    for endpoint, values in durations.items():
        avg = sum(values) / len(values)
        table.append({"url": endpoint, "average_duration": round(avg, 2)})
    return table

REPORT_GENERATORS = {
    "average": generate_average_report,
}

def generate_report(report_type, logs):
    if report_type not in REPORT_GENERATORS:
        raise ValueError(f"Неподдерживаемый тип отчета: {report_type}")
    return REPORT_GENERATORS[report_type](logs)

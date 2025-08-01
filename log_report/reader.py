import json

def read_logs(file_paths, date_filter=None):
    logs = []
    for path in file_paths:
        with open(path, "r") as f:
            for line in f:
                try:
                    log_entry = json.loads(line.strip())
                    if date_filter:
                        timestamp = log_entry.get("@timestamp")
                        if not timestamp or not timestamp.startswith(date_filter):
                            continue
                    logs.append(log_entry)
                except json.JSONDecodeError:
                    # Пропускаем некорректные строки
                    continue
    return logs

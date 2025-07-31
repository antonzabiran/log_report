import json

def read_logs(file_paths):
    logs = []
    for path in file_paths:
        with open(path, "r") as f:
            for line in f:
                try:
                    log_entry = json.loads(line.strip())
                    logs.append(log_entry)
                except json.JSONDecodeError:
                    continue  # Пропустить некорректные строки
    return logs

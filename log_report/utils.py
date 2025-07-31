import os
from tabulate import tabulate

def validate_file_paths(file_paths):
    return all(os.path.isfile(path) for path in file_paths)

def print_table(report_data):
    headers = ["Endpoint", "Request Count", "Avg Response Time"]
    print(tabulate(report_data, headers=headers, tablefmt="grid"))
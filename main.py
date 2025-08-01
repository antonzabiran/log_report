import argparse
import sys
from utils import validate_file_paths
from reader import read_logs
from report import generate_report
from tabulate import tabulate

def main():
    parser = argparse.ArgumentParser(description="Генерация отчета по логам")
    parser.add_argument("--file", nargs='+', required=True, help="Пути к лог-файлам")
    parser.add_argument("--report", required=True, help="Тип отчета (например: average)")
    parser.add_argument("--date", required=False, help="Фильтр по дате (YYYY-MM-DD)")
    args = parser.parse_args()

    try:
        validate_file_paths(args.file)
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)

    logs = read_logs(args.file, args.date)

    try:
        table = generate_report(args.report, logs)
    except ValueError as e:
        print(e)
        sys.exit(1)

    print(tabulate(table, headers="keys"))

if __name__ == "__main__":
    main()

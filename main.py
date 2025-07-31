import argparse
from log_report.reader import read_logs
from log_report.report import generate_average_report
from log_report.utils import validate_file_paths, print_table


def main():
    parser = argparse.ArgumentParser(description="Log report generator")
    parser.add_argument("--file", nargs="+", required=True, help="Path to log file(s)")
    parser.add_argument("--report", required=True, help="Report type (only 'average' supported)")

    args = parser.parse_args()

    # Валидация входных путей к файлам
    if not validate_file_paths(args.file):
        print("One or more log files do not exist.")
        return

    # Чтение логов
    logs = read_logs(args.file)

    # Обработка отчета по типу
    if args.report == "average":
        report_data = generate_average_report(logs)
        print_table(report_data)
    else:
        print("Unsupported report type")


if __name__ == "__main__":
    main()
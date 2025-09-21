import os

from argparse import Namespace, ArgumentParser
from typing import Callable

from app.utils import get_data, generate_report_grade


REPORTS: dict[str, Callable] = {
    "students-performance": generate_report_grade
}


def get_parser_args() -> Namespace:
    """
    Получение аргументов из командной строки.
    """
    parser = ArgumentParser(description="Parser_csv")

    parser.add_argument(
        "--files",
        nargs="+",
        type=str,
        required=True,
        help="List of CSV files to process"
    )

    parser.add_argument(
        "--report",
        type=str,
        required=True,
        help="Type of report to generate"
    )

    return parser.parse_args()


def output_report(args: Namespace) -> None:
    """
    Выводит необходимый отчет, указанный в командной строке.
    """
    report_type = args.report

    if report_type not in REPORTS:
        raise ValueError(f"Неизвестный тип отчета: {report_type}")

    for filename in args.files:
        if not os.path.isfile(filename):
            raise FileNotFoundError(
                f"Файл {filename} не найден. "
                "Попробуйте указать полный путь."
            )

    records = get_data(args)
    print(REPORTS[report_type](records))


if __name__ == "__main__":
    try:
        args = get_parser_args()
        output_report(args)
    except FileNotFoundError as exc:
        print(f"Ошибка: {exc}")
    except Exception as exc:
        print(f"Возникла непредвиденная ошибка: {exc}")

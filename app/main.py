import os
from argparse import Namespace
from typing import Callable

from app.parser import get_parser_args
from app.generators_reports import GeneratorReportRating


# Словарь с доступными отчетами и классами для их формирования
REPORTS: dict[str, Callable] = {
    "average-rating": GeneratorReportRating
}


def main(args: Namespace) -> None:
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

    print(REPORTS[report_type](args).generate_report())


if __name__ == "__main__":
    try:
        args = get_parser_args()
        main(args)
    except Exception as exc:
        print(f"Возникла непредвиденная ошибка: {exc}")

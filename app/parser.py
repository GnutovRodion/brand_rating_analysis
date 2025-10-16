from argparse import Namespace, ArgumentParser


def get_parser_args() -> Namespace:
    """
    Получение аргументов из командной строки.
    """
    parser = ArgumentParser(description="Parser_CSV")

    parser.add_argument(
        "--files",
        nargs="+",
        type=str,
        required=True,
        help="Список CSV-файлов"
    )

    parser.add_argument(
        "--report",
        type=str,
        required=True,
        help="Название отчета"
    )

    return parser.parse_args()

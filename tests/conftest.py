from argparse import Namespace

import pytest

from app.generators_reports import GeneratorReportRating


@pytest.fixture(scope="session")
def output_data_rating() -> list[str]:
    """
    Фикстура для подготовки тестовых данных из генератора отчетов.
    """
    args = Namespace(
        files=["tests/test_data.csv"],
        report="average-rating"
    )
    output = GeneratorReportRating(args).generate_report()
    return output.splitlines()

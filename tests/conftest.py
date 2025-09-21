import csv
import pytest

from app.utils import StudentRecord


@pytest.fixture(scope="session")
def get_test_data() -> list[StudentRecord]:
    """
    Фикстура для парсинга тестовых данных в унифицированную структуру.
    """
    test_data = []

    with open("tests/test_data.csv", "r", encoding="utf-8") as test_file:
        reader = csv.DictReader(test_file)
        for row in reader:
            test_data.append(StudentRecord(
                    student_name=row["student_name"],
                    subject=row["subject"],
                    teacher_name=row["teacher_name"],
                    date=row["date"],
                    grade=float(row["grade"])
                ))

    return test_data

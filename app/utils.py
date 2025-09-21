import csv
from argparse import Namespace
from collections import defaultdict
from dataclasses import dataclass

from tabulate import tabulate


@dataclass
class StudentRecord:
    """
    Запись с информацией о студентах.
    """
    student_name: str
    subject: str
    teacher_name: str
    date: str
    grade: float


def get_data(args: Namespace) -> list[StudentRecord]:
    """
    Парсит данные в унифицированную структуру.
    """
    data = []

    for file_path in args.files:

        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(StudentRecord(
                    student_name=row["student_name"],
                    subject=row["subject"],
                    teacher_name=row["teacher_name"],
                    date=row["date"],
                    grade=float(row["grade"])
                ))

    return data


def generate_report_grade(records: list[StudentRecord]) -> str:
    """
    Формирует отчет успеваемости студентов.
    """
    data: dict[str, list[float]] = defaultdict(list)

    for record in records:
        data[record.student_name].append(record.grade)

    result_list: list[tuple[str, float]] = [
        (name, round(sum(grades)/len(grades), 2))
        for name, grades in data.items()
    ]

    result_list.sort(key=lambda x: x[1], reverse=True)

    return tabulate(
        [(i, row[0], row[1]) for i, row in enumerate(result_list, 1)],
        headers=["student_name", "grade"],
        tablefmt="github",
        numalign="right",
        stralign="left"
    )


from app.utils import generate_report_grade, StudentRecord


def test_output_report_grade(get_test_data: list[StudentRecord]) -> None:
    """
    Тест корректности содержания отчета успеваемости.
    """
    output = generate_report_grade(get_test_data)
    lines = output.splitlines()

    assert (
        len(lines) == 5
    ), "Количество строк в отчете не соответсвует ожидаемому."
    headers = [col.strip() for col in lines[0].split("|") if col.strip()]

    assert headers == [
        "student_name", "grade"
    ], "Заголовки в отчете не соответсвуют ожидаемым."

    column = [col.strip() for col in lines[3].split("|") if col.strip()]
    student_record = dict(zip(headers, column[1:]))

    assert (
        student_record["student_name"] == "Семенова Елена"
    ), "Содержание отчета не соответствует структуре."
    assert (
        student_record["grade"] == "4.5"
    ), "Средняя оценка студента не соответсвует ожидаемой."


def test_ordering_grades(get_test_data: list[StudentRecord]) -> None:
    """
    Тест сортировки записей в отчете по успеваемости.
    """
    output = generate_report_grade(get_test_data)
    lines = output.splitlines()

    grades = []

    for line in lines[2:]:
        columns = [col.strip() for col in line.split("|") if col.strip()]
        grades.append(float(columns[2]))

    assert (
        grades == sorted(grades, reverse=True)
    ), "Записи должны быть отсортированы по убыванию средней оценки студента."

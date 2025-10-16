def test_output_report_grade(output_data_rating: list[str]) -> None:
    """
    Тест корректности содержания отчета рейтинга брендов.
    """

    assert (
        len(output_data_rating) == 5
    ), "Количество строк в отчете не соответсвует ожидаемому."
    headers = [
        col.strip() for col in output_data_rating[0].split("|") if col.strip()
    ]

    assert headers == [
        "brand", "rating"
    ], "Заголовки в отчете не соответсвуют ожидаемым."

    column = [
        col.strip() for col in output_data_rating[3].split("|") if col.strip()
    ]
    student_record = dict(zip(headers, column[1:]))

    assert (
        student_record["brand"] == "xiaomi"
    ), "Содержание отчета не соответствует структуре."
    assert (
        student_record["rating"] == "4.6"
    ), "Средний рейтинг бренда не соответсвует ожидаемому."


def test_ordering_grades(output_data_rating: list[str]) -> None:
    """
    Тест сортировки записей в отчете рейтингов брендов.
    """

    grades = []

    for line in output_data_rating[2:]:
        columns = [col.strip() for col in line.split("|") if col.strip()]
        grades.append(float(columns[2]))

    assert (
        grades == sorted(grades, reverse=True)
    ), "Записи должны быть отсортированы по убыванию среднего рейтинга бренда."

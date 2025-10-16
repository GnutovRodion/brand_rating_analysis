from collections import defaultdict

from tabulate import tabulate

from app.base_generator import BaseGeneratorReport


class GeneratorReportRating(BaseGeneratorReport):
    """
    Формирует отчет рейтинга брендов.
    """
    def generate_report(self) -> str:
        data: dict[str, list[float]] = defaultdict(list)

        for product in self.products:
            data[product.brand].append(product.rating)

        result_list: list[tuple[str, float]] = [
            (brand, round(sum(ratings)/len(ratings), 2))
            for brand, ratings in data.items()
        ]

        result_list.sort(key=lambda x: x[1], reverse=True)

        return tabulate(
            [(i, row[0], row[1]) for i, row in enumerate(result_list, 1)],
            headers=["brand", "rating"],
            tablefmt="github",
            numalign="right",
            stralign="left"
        )

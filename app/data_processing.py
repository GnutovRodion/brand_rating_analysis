import csv
from argparse import Namespace
from dataclasses import dataclass


@dataclass
class BrandRecord:
    """
    Запись с информацией о брендах.
    """
    name: str
    brand: str
    price: float
    rating: float


class DataPreparation:
    """
    Подготовка данных для обработки.
    """
    def __init__(self, args):
        self.args: Namespace = args
        self.products: list[BrandRecord] = []
        self._get_data(self.args.files)

    def _get_data(self, files: list[str]) -> None:
        """
        Парсит данные в унифицированную структуру.
        """
        for file_path in files:

            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.products.append(BrandRecord(
                        name=row["name"],
                        brand=row["brand"],
                        price=float(row["price"]),
                        rating=float(row["rating"])
                    ))

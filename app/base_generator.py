from abc import ABC, abstractmethod

from app.data_processing import DataPreparation


class BaseGeneratorReport(ABC, DataPreparation):
    """
    Абстрактный класс для формирования необходимого отчета.
    """

    @abstractmethod
    def generate_report(self):
        pass

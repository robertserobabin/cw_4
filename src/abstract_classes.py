from abc import ABC, abstractmethod


class JobParser(ABC):
    @abstractmethod
    def get_vacancies(self, params):
        pass


class AbstractFileSaver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

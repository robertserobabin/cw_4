import json
from src.abstract_classes import AbstractFileSaver


class JSONSaver(AbstractFileSaver):
    def __init__(self, filename: str = 'vacancies.json') -> None:
        self.filename = filename

        with open(self.filename, 'w', encoding='utf-8') as file:
            file.write(json.dumps([], indent=2, ensure_ascii=False))

    def add_vacancy(self, vacancy) -> None:
        """Метод для добавления вакансий в JSON формате в файл vacancies.json"""

        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(vacancy, file, indent=2, ensure_ascii=False)

    def get_vacancies(self) -> None:
        """Метод для получения вакансий из файла vacancies.json"""

        with open(self.filename, 'w', encoding='utf-8') as file:
            return json.load(file)

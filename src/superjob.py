import requests
from src.abstract_classes import JobParser
from src.config import API_SECRET_KEY
from http import HTTPStatus


class SuperJobAPI(JobParser):
    def get_vacancies(self, params):
        """Метод для получения вакансий в формате JSON"""

        headers = {
            "X-Api-App-Id": API_SECRET_KEY
        }
        params = {
            "keyword": 'python',
            "page": "1"
        }
        response = requests.get("https://api.superjob.ru/2.0/vacancies/",
                                params=params,
                                headers=headers)
        if not response.status_code == HTTPStatus.OK:
            return f'Ошибка! Статус-код: {response.status_code}'
        return response.json()['objects']

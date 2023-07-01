import pytest

from src.vacancy import Vacancy


@pytest.fixture
def instance_vacancy():
    return Vacancy('Python разработчик', 'ссылка', '100', 'от 1 года')


def test_str(instance_vacancy):
    assert str(instance_vacancy) == f'Название: Python разработчик\n' \
                                    f'Ссылка: ссылка\n' \
                                    f'Зарплата: 100\n' \
                                    f'Требования: от 1 года'


def test_repr(instance_vacancy):
    assert repr(instance_vacancy) == f'Vacancy(' \
               f'title=Python разработчик, ' \
               f'url=ссылка, ' \
               f'salary=100, ' \
               f'requirements=от 1 года)'

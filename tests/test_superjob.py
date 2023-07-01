from src.superjob import SuperJobAPI


def test_get_vacancies():
    assert isinstance(SuperJobAPI().get_vacancies('Python'), list)

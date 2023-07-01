from src.headhunter import HeadHunterAPI


def test_get_vacancies():
    assert isinstance(HeadHunterAPI().get_vacancies('Python'), list)

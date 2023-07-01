from src.headhunter import HeadHunterAPI
from src.superjob import SuperJobAPI
from src.json_saver import JSONSaver
from src.utils import filter_vacancies, sort_vacancies, get_top_vacancies, print_vacancies

hh_api = HeadHunterAPI()
sj_api = SuperJobAPI()

hh_vacancies = hh_api.get_vacancies("Python")
sj_vacancies = sj_api.get_vacancies("Python")


# Функция для взаимодействия с пользователем
def user_interaction():
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ")
    filtered_vacancies = filter_vacancies(hh_vacancies, sj_vacancies, filter_words)
    json_saver = JSONSaver()

    if not filtered_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    sorted_vacancies = sort_vacancies(filtered_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)
    json_saver.add_vacancy(top_vacancies)


if __name__ == "__main__":
    user_interaction()

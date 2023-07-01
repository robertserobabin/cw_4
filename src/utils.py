def filter_vacancies(hh_vacancies, sj_vacancies, filtered_words) -> list:
    hh_data = []
    for hh_vacancy in hh_vacancies:
        if filtered_words.lower() in hh_vacancy['name'].lower():
            if hh_vacancy['salary'] is not None:
                if hh_vacancy['salary']['from'] is None:
                    hh_data.append(
                        f'{hh_vacancy["name"]}\nСсылка: {hh_vacancy["alternate_url"]}\n'
                        f'Заработная плата: до {hh_vacancy["salary"]["to"]}\n'
                        f'Требуемый опыт: {hh_vacancy["experience"]["name"]}')
                elif hh_vacancy['salary']['to'] is None:
                    hh_data.append(
                        f'{hh_vacancy["name"]}\nСсылка: {hh_vacancy["alternate_url"]}\n'
                        f'Заработная плата: от {hh_vacancy["salary"]["from"]}\n'
                        f'Требуемый опыт: {hh_vacancy["experience"]["name"]}')
                else:
                    hh_data.append(
                        f'{hh_vacancy["name"]}\nСсылка: {hh_vacancy["alternate_url"]}\n'
                        f'Заработная плата: от {hh_vacancy["salary"]["from"]} до: {hh_vacancy["salary"]["to"]}\n'
                        f'Требуемый опыт: {hh_vacancy["experience"]["name"]}')
            else:
                hh_data.append(
                    f'{hh_vacancy["name"]}\nСсылка: {hh_vacancy["alternate_url"]}\nЗаработная плата: Не указано.\n'
                    f'Требуемый опыт: {hh_vacancy["experience"]["name"]}')

    sj_data = []
    for sj_vacancy in sj_vacancies:
        if filtered_words.lower() in sj_vacancy['profession'].lower():
            if sj_vacancy['payment_from'] == 0:
                sj_data.append(f'{sj_vacancy["profession"]}\nСсылка: {sj_vacancy["link"]}\n'
                               f'Заработная плата: до {sj_vacancy["payment_to"]}\n'
                               f'Требуемый опыт: {sj_vacancy["experience"]["title"]}')
            elif sj_vacancy['payment_to'] == 0:
                sj_data.append(f'{sj_vacancy["profession"]}\nСсылка: {sj_vacancy["link"]}\n'
                               f'Заработная плата: от {sj_vacancy["payment_from"]}\n'
                               f'Требуемый опыт: {sj_vacancy["experience"]["title"]}')
            else:
                sj_data.append(f'{sj_vacancy["profession"]}\nСсылка: {sj_vacancy["link"]}\n'
                               f'Заработная плата: от {sj_vacancy["payment_from"]}, до {sj_vacancy["payment_to"]}\n'
                               f'Требуемый опыт: {sj_vacancy["experience"]["title"]}')

    vacancies = []
    vacancies.extend(hh_data)
    vacancies.extend(sj_data)
    return vacancies


def sort_vacancies(vacancies: list) -> list:
    return sorted(vacancies)


def get_top_vacancies(vacancies: list, number_of_top: int) -> list:
    return vacancies[:number_of_top]


def print_vacancies(vacancies: list) -> None:
    for vacancy in vacancies:
        print(vacancy)
        print()

class Vacancy:
    vacancy_list = []

    def __init__(self, title: str, url: str, salary: str, requirements: str) -> None:
        self.validate_attributes(title, url, salary, requirements)

        self.__title = title
        self.__url = url
        self.__salary = salary
        self.__requirements = requirements
        self.vacancy_list.append(self)

    def __str__(self) -> str:
        return f'Название: {self.title}\nСсылка: {self.url}\nЗарплата: {self.salary}\nТребования: {self.requirements}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(' \
               f'title={self.title}, ' \
               f'url={self.url}, ' \
               f'salary={self.salary}, ' \
               f'requirements={self.requirements})'

    def __gt__(self, other_instance) -> bool:
        return self.salary.split > other_instance.salary

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, other_title: str) -> None:
        if isinstance(other_title, str):
            self.title = other_title

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, other_url: str) -> None:
        if isinstance(other_url, str):
            self.url = other_url

    @property
    def salary(self) -> str:
        return self.__salary

    @salary.setter
    def salary(self, other_salary: str) -> None:
        if isinstance(other_salary, str):
            self.salary = other_salary

    @property
    def requirements(self) -> str:
        return self.__requirements

    @requirements.setter
    def requirements(self, other_requirements: str) -> None:
        if isinstance(other_requirements, str):
            self.requirements = other_requirements

    @staticmethod
    def validate_attributes(title: str, url: str, salary: str, requirements: str) -> None:
        """Статический метод для валидации атрибутов класса"""

        if not isinstance(title, str):
            raise TypeError('Название вакансии должно передаваться быть строкой.')
        if not isinstance(url, str):
            raise TypeError('Передаваемая ссылка должна быть строкой.')
        if not isinstance(salary, str):
            raise TypeError('Зарплата должна передаваться строкой в формате "xxx-yyy"')
        if not isinstance(requirements, str):
            raise TypeError('Требования должны передаваться строкой.')

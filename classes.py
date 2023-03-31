from abc import ABC, abstractmethod
import requests
import re
import os
from connector import Connector


class Engine(ABC):
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0"
    }

    @abstractmethod
    def get_request(self) -> None:
        pass


class HH(Engine):
    API = "https://api.hh.ru/vacancies/"

    def __init__(self, keyword: str) -> None:
        self.keyword = keyword

    def get_request(self, page: int) -> dict:
        params = {
            "area": 113,
            "page": page,
            "per_page": 100,
            "text": f"{self.keyword}",
            "experience": "noExperience",
        }
        return requests.get(url=self.API, params=params, headers=self.HEADERS).json()[
            "items"
        ]

    @property
    def answer(self) -> list:
        vacancy_list = []
        for ans in range(0, 5):
            answer = self.get_request(ans)
            for i in answer:
                vacancy_list.append(i)
        return vacancy_list


class Superjob(Engine):
    API_KEY = os.getenv("SJ_KEY")
    my_auth_data = {"X-Api-App-Id": API_KEY}

    def __init__(self, keyword: str):
        self.keyword = keyword

    def get_request(self, page: int) -> dict:
        return requests.get(
            "https://api.superjob.ru/2.0/vacancies/",
            headers=self.my_auth_data,
            params={"keywords": f"{self.keyword}", "page": 0, "per_page": 20},
        ).json()["objects"]

    @property
    def answer(self) -> list:
        vacancy_list = []
        for ans in range(25):
            answer = self.get_request(ans)
            for i in answer:
                vacancy_list.append(i)
        return vacancy_list


class Vacancy:
    def __init__(self, name: str, url: str, desc: str, salary: int):
        self.name = name
        self.url = url
        self.desc = desc
        self.salary = salary

    def args_parsing(self) -> None:
        if self.desc != None:
            self.desc = self.desc.partition(".")[0]
            self.desc = self.desc.replace("\n", "")
            self.desc = re.sub(r"\<[^>]*\>", "", self.desc)
        if self.salary == None:
            self.salary = 0
        if type(self.salary) is dict:
            self.salary = self.salary["from"]
            if self.salary == None:
                self.salary = 0

    def to_json(self) -> dict:
        self.args_parsing()
        return {
            "name": self.name,
            "salary": self.salary,
            "description": self.desc,
            "url": self.url,
        }

    def __repr__(self) -> str:
        return f"Вакансия: {self.name}, Зарплата: {self.salary}, Описание: {self.desc}, Ссылка: {self.url}"

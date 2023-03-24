from abc import ABC, abstractmethod
import requests
import json
import os
from connector import Connector

class Engine(ABC):
    HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0'}

    @abstractmethod
    def get_request(self):
        return requests.get(url=self.API, params=self.params, headers=self.HEADERS).json()

    @staticmethod
    def get_connector(file_name: str) -> Connector:
        connector = Connector(file_name)
        """ Возвращает экземпляр класса Connector """
        return connector

class HH(Engine):

    API = 'https://api.hh.ru/vacancies/'

    def __init__(self, keyword):
        self.keyword = keyword

    def get_request(self, page):
        params = {
            'area': 113,
            'page': page,
            'per_page': 100,
            'text': f'{self.keyword}',
            'experience': 'noExperience'
        }
        return requests.get(url=self.API, params=params, headers=self.HEADERS).json()['items']

    @property
    def answer(self):
        vacancy_list = []
        for ans in range(0,5):
            answer = self.get_request(ans)
            for i in answer:
                vacancy_list.append(i)
        return vacancy_list




class Superjob(Engine):
    def get_request(self):
        pass


class Vacancy():

    def __init__(self, name, url, desc, salary):
        self.name = name
        self.url = url
        self.salary = salary
        self.desc = desc

    def to_json(self):
        return {'name': self.name, 'salary': self.salary, 'description': self.desc, 'url': self.url}

    def __repr__(self):
        return f'Вакансия: {self.name}, Зарплата: {self.salary}, Описание: {self.desc}, Ссылка: {self.url}'


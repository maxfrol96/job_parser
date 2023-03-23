from abc import ABC, abstractmethod
import requests
import json
import os
from connector import Connector

class Engine(ABC):
    HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0'}

    @abstractmethod
    def get_request(self):
        pass

    @staticmethod
    def get_connector(file_name: str) -> Connector:
        connector = Connector(file_name)
        """ Возвращает экземпляр класса Connector """
        return connector

class HH(Engine):

    API = 'https://api.hh.ru/vacancies/'

    def __init__(self, keyword):
        self.keyword = keyword
        self.params = {
            'area': 113,
            'page': 1,
            'per_page': 1,
            'text': f'{self.keyword}',
                }
        self.name = self.get_request()['items'][0]['name']
        self.url = self.get_request()['items'][0]['alternate_url']
        self.salary = self.get_request()['items'][0]['salary']['from']
        self.description = self.get_request()['items'][0]['snippet']['requirement']

    def __repr__(self):
        return



    def get_request(self):
        return requests.get(url=self.API, params=self.params, headers=self.HEADERS).json()




class Superjob(Engine):
    def get_request(self):
        pass


class Vacancy():
    pass



a = Connector()
a.data_file

vac = HH('python')
print(vac.name)
print(vac.url)
print(vac.get_request())
print(vac.salary)
print(vac.description)
# params = {
#         'area': 113,
#         'page': 1,
#         'per_page': 3,
#         'text': 'python',
#     }
# url = 'https://api.hh.ru/vacancies/'
# HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0'}
# answ = requests.request(method='GET', url=url, params=params, headers=HEADERS)
# print(answ)
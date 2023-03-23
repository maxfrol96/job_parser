class Connector:
    """
    Класс коннектор к файлу, обязательно файл должен быть в json формате
    не забывать проверять целостность данных, что файл с данными не подвергся
    внешнего деградации
    """
    __data_file = None
    @property
    def data_file(self):
        return self.__data_file

    @data_file.setter
    def data_file(self):
        return self.__connect()

    def __connect(self):
        file = open('vacancy_list.json', 'w+')
        file.write('abc')
        file.close()
        return file

    def insert(self, data):
        """
        Запись данных в файл с сохранением структуры и исходных данных
        """
        pass

    def select(self, query):
        """
        Выбор данных из файла с применением фильтрации
        query содержит словарь, в котором ключ это поле для
        фильтрации, а значение это искомое значение, например:
        {'price': 1000}, должно отфильтровать данные по полю price
        и вернуть все строки, в которых цена 1000
        """
        pass

    def delete(self, query):
        """
        Удаление записей из файла, которые соответствуют запрос,
        как в методе select. Если в query передан пустой словарь, то
        функция удаления не сработает
        """
        pass

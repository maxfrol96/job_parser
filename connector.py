import json


class Connector:
    """
    Класс коннектор к файлу, обязательно файл должен быть в json формате
    не забывать проверять целостность данных, что файл с данными не подвергся
    внешнего деградации
    """

    __data_file = None

    @property
    def data_file(self) -> None:
        return self.__data_file

    @data_file.setter
    def data_file(self, name: str) -> None:
        file = open(f"{name}.json", "a+")
        file.close()
        self.__data_file = file.name

    def insert(self, data: str) -> None:
        with open(f"{self.data_file}", "w+", encoding="utf-8") as file:
            json_data = json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4)
            file.write(json_data)

    def select(self, query: dict) -> list:
        with open(f"{self.data_file}", "r", encoding="utf-8") as file:
            data = json.load(file)
            query_items = list(query.items())[0]
            query_key = query_items[0]
            query_value = query_items[1]
            answer = []
            for vac in data["items"]:
                if vac["vacancy"][query_key] == query_value:
                    answer.append(vac)
            return answer

    def delete(self, query: dict) -> None:
        with open(f"{self.data_file}", "r+", encoding="utf-8") as file:
            data = json.load(file)
            query_items = list(query.items())[0]
            query_key = query_items[0]
            query_value = query_items[1]
            for vac in data["items"]:
                if vac["vacancy"][query_key] == query_value:
                    data["items"].remove(vac)
            json_data = json.dumps(data, ensure_ascii=False)
        with open(f"{self.data_file}", "w", encoding="utf-8") as file:
            file.write(json_data)

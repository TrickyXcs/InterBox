import requests 
from tabulate import tabulate


class CountryApi:
    def __init__(self):
        self.url = 'https://restcountries.com/v3.1/all/'

    def get_data(self) -> list:
        response = requests.get(f"{self.url}?fields=name,capital,flags")
        return response.json()

    def clean_data(self, data: list) -> list:
        cleaned_data = []
        for instance in data:
            country = instance["name"]["official"]
            capital = instance["capital"]
            flag_url = instance["flags"]["png"]
            if len(capital) == 0:
                capital.append("Немає")
            elif len(capital) > 1:
                capital = [",".join(capital)]
            cleaned_data.append([country, *capital, flag_url])
        return cleaned_data
    
    def get_table(self) -> str:
        data = self.get_data()
        clean_data = self.clean_data(data)
        return tabulate(clean_data, headers=["Країна","Столиця","Прапор"])

    def print_table(self):
        table = self.get_table()
        print(table)

api = CountryApi()
api.print_table()
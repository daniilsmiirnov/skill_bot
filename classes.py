import requests
import json
from values import *


class APIException(Exception):
    pass


class Converter:
    @staticmethod
    def get_price(val1: str, val2: str, num: float):
        if val1 == val2:
            raise APIException('Нельзя переводить одинаковые валюты')

        try:
            valu1 = currency[val1]
        except KeyError:
            raise APIException('Неудалось обработать валюту')
        try:
            valu2 = currency[val2]
        except KeyError:
            raise APIException('Неудалось обработать валюту')
        try:
            numb = float(num)
        except ValueError:
            raise APIException('Неудалось обработать количество')

        r = requests.get(
            f'https://min-api.cryptocompare.com/data/price?fsym={valu1}&tsyms={valu2}')
        price = json.loads(r.content)[currency[val2]]
        price = float(price)*float(num)
        return price

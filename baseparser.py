from bs4 import BeautifulSoup
import requests


class BaseParser:
    def __init__(self):
        self.url = 'https://olcha.uz/ru/discounts'
        self.host = 'https://olcha.uz'

    def get_html(self, url=None):
        """Метод получения HTML по ссылке
        Если ссылку не подали - используем свою по умолчанию"""
        if url:
            return requests.get(url).text
        else:
            return requests.get(self.url).text

    def get_soup(self, html):
        """Метод преобразования html в soup объект"""
        return BeautifulSoup(html, 'html.parser')

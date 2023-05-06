import requests #для обращения к какому либо ресурсу
from bs4 import BeautifulSoup #разбирает html страницу, делает из нее объект, с которым мы потом работаем
import csv #создает csv файл, который можно будет открыть в excel

HOST = "https://gepur.com/"
URL = "https://gepur.com/catalog/platya"
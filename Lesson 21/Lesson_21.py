#Функция скачивания изображений

import random
import urllib.request
names = []

def download_img(url):
    name = random.randrange(1, 100)
    name = str(name) + ".jpg"
    for name in names:
        print ("Совпадение имен")
        name = str(name)+"2"+".jpg"
    urllib.request.urlretrieve(url, name)

download_img("https://ichef.bbci.co.uk/news/640/cpsprodpb/14A82/production/_116301648_gettyimages-1071204136.jpg")
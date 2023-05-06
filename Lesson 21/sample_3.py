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

download_img("http://pikstok.ru/images/images/1528372927887.jpg")
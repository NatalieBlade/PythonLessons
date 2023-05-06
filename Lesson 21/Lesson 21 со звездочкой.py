import random
import urllib.request
import urllib.error
names = []

def download_img(url):
    name = random.randrange(1, 10)
    name = str(name) + ".jpg"
    if name in names:
        name = str(name)+"2"+".jpg"
    else:
        names.append(name)
    urllib.request.urlretrieve(url, name)
try:
    download_img("http:/pikstok.ru/images/images/1528372927887.jpg") #не хватает / после http:
except urllib.error.URLError:
    download_img("https://ichef.bbci.co.uk/news/640/cpsprodpb/14A82/production/_116301648_gettyimages-1071204136.jpg")
    print('Ошибка при скачивании')
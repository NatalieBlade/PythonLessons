import random
import urllib.request

filenames = []

try:
    def download_img(url):
        name = random.randrange(1, 10)
        filenames.append(name)
        name = str(name) + '.jpg'

        for element in filenames:
            if element == name:
                continue
            else:
                name = str(name) + "2" + ".jpg"

    urllib.request.urlretrieve(url, name)

    download_img("https://ichef.bbci.co.uk/news/640/cpsprodpb/14A82/production/_116301648_gettyimages-1071204136.jpg")
except:
    print('не удалось скачать')

print(filenames)
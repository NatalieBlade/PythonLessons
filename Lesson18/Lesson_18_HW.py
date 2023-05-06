import time, random
import textwrap
import uuid
#import emo
import colorsys
import colorama_
#from colorama_ import init
#init()
print (uuid.uuid4())
print(time.time())
print(random.random())
x = textwrap.dedent("Hello, world!")
print(x)
print(colorsys.hls_to_rgb(5, 7, 2))
#warnings.filterwarnings(float, hex(7), list, time)


# import fuzzywuzzy
# f = fuzzywuzzy.ratio("Hello", "Jalle")
# print(f)

# import wget
# x = wget.download("http://www.ozon.ru")
# print(x)

# from snowballstemmer import EnglishStemmer, SpanishStemmer
# EnglishStemmer().stemWord("Gregory")
# SpanishStemmer().stemWord("amarillo")


import urllib
import requests
import re

page = "https://noticias.uol.com.br/ultimas/"
html = requests.get(page).text
lista = re.findall(r'<h3 class="thumb-title title-xsmall title-lg-small"[^>]*>(.*?)</h3>',html)
noticias=''
for i in lista:
    noticias+=i+'\n\n'

print(noticias)

'''<h3 class="thumb-title title-xsmall title-lg-small"> Batel, Cabral, Cristo Rei, Bacacheri e mais 10 bairros de Curitiba sem água neste domingo </h3>'''



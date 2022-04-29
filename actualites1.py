import re
from bs4 import BeautifulSoup
import requests

metiers = []
dates = []
entreprises = []
descriptions = []
regions = []
liens =[]
websites = []
images = []
values = []


class ActuCote:

    documents = requests.get("https://abidjan.net/").text
    soup = BeautifulSoup(documents, 'lxml')

    regs = soup.find_all('a', class_='grd-item ebloc-big')

   


    def datas(self):
            for reg in self.regs:
                descriptions.append(reg.find('span', class_='title').text)
                liens.append(reg.get('href'))
                websites.append("abidjan.net")
            for i in range(len(liens)):
                values.append({'site':websites[i],'lien':liens[i], 'description':descriptions[i]})
            return values


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


class Content:

    documents = requests.get("https://ludoviccreative.com/").text
    soup = BeautifulSoup(documents, 'lxml')

    regs = soup.find_all('h2', class_='is-title post-title')

    def datas(self):
        for reg in self.regs:
                    descriptions.append(reg.text)
                    liens.append(reg.find('a').get('href'))
                    websites.append("ludoviccreative.com")
        for i in range(len(liens)):
            values.append({'site':websites[i],'lien':liens[i], 'description':descriptions[i]})
        return values



      

    
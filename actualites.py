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


class Base:

    documents = requests.get("https://actumusikafrika.com/").text
    soup = BeautifulSoup(documents, 'lxml')

    regs = soup.find_all('h3', class_='entry-title')

 

    def datas(self):
        for reg in self.regs:
            descriptions.append(reg.text)
            liens.append(reg.find('a').get('href'))
            websites.append("actumusikafrika.com")
        for i in range(len(liens)):
            values.append({'site':websites[i],'lien':liens[i], 'description':descriptions[i]})
        return values







    #def sites(self):
            #for title in self.titles:
            #  websites.append("emploi.cm")
            #return websites
            
        #print(documents)

  
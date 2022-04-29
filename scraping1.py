from bs4 import BeautifulSoup
import requests
from scraping import elements
from scraping2 import elements2
from scraping3 import elements3
import random



class datas:
    el = elements()
    el2 = elements2()
    el3 = elements3()
    values = []
    
    taille = el.taille() + el2.taille() + el3.taille()
    metiers = el.metier() + el2.metier() + el3.metier()
    descriptions = el.description() + el2.description() + el3.description()
    liens = el.lien() + el2.lien() + el3.lien()
    sites = el.sites() + el2.sites() + el3.sites()
    

    def data(self):
        for i in range(self.taille):
            self.values.append({'site':self.sites[i],'lien':self.liens[i], 'metier':self.metiers[i], 'description':self.descriptions[i]})
        self.values = random.sample(self.values, len(self.values))
        return self.values

    def tailles(self):
        return self.taille

"""
metiers = []
dates = []
entreprises = []
descriptions = []
regions = []
liens =[]

documents = requests.get("https://www.jobinfocamer.com/jobs/").text
soup = BeautifulSoup(documents, 'lxml')

titles = soup.find_all('strong')

for title in titles:
    metiers.append(title.text)


#for i in range(len(metiers) -1):
  # print(metiers[i])
  

times = soup.find_all('td', class_='text-nowrap')

for time in times:
    dates.append(time.text)


#for i in range(len(dates)):
   #print(dates[i])

body = soup.find_all('tr')
for bodi in body:
    liens.append("https://www.jobinfocamer.com" + bodi.find('a').get('href'))

#for lien in liens:
    #print(lien)

for bodi in body:
    entreprises.append(bodi.find('p').text)

"""


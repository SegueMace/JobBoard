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

class elements:

    documents = requests.get("https://www.emploi.cm/recherche-jobs-cameroun/").text
    soup = BeautifulSoup(documents, 'lxml')

    titles = soup.find_all('h5')

    def metier(self):
        for title in self.titles:
            metiers.append(title.text)
        return metiers


    def sites(self):
         for title in self.titles:
            websites.append("emploi.cm")
         return websites
        
    #print(documents)


    datas = soup.find_all('p', class_='job-recruiter')

    
    for data in datas:
        dates.append((data.text).split('|')[0])


    for data in datas:
        entreprises.append((data.text).split('|')[1])


    descs = soup.find_all('div', class_='search-description')

    def description(self):
        for desc in self.descs:
            descriptions.append(desc.text)
        return descriptions

    regs = soup.find_all('p', attrs={'class': None})

    for reg in regs:
        regions.append(reg.text)


    a = soup.find_all('div', class_='job-description-wrapper') 
  

    def lien(self):
        for i in self.a:
            liens.append(i.get('data-href'))
        return liens


   
    #for i in range(len(metiers)):
    #   print(metiers[i])
    #  print(dates[i])
    # print(entreprises[i])
        #print(descriptions[i])
        #print(regions[i])
        #print(liens[i]) 



    #Fin de scraping pour emploi.cm
    def taille(self):
        return len(self.lien())


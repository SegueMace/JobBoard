from bs4 import BeautifulSoup
import requests

metiers = []
dates = []
entreprises = []
descriptions = []
regions = []
liens =[]
websites = []

class elements2:
    documents = requests.get("https://www.offre-emploi.cm/").text
    soup = BeautifulSoup(documents, 'lxml')


    datas = soup.find_all('div', class_='jobTitle')
    descs = soup.find_all('div', class_='preview')

    def metier(self):
        for data in self.datas:
            metiers.append(data.text)
        return metiers

    def description(self):
        for desc in self.descs:
            descriptions.append(desc.text)
        return descriptions


    #for i in range(len(metiers)):
    #  print(metiers[i])


    def lien(self):
        for data in self.datas:
            liens.append(data.find('a').get('href'))
        return liens
    

    def taille(self):
        return len(self.lien())
    
    def sites(self):
        for desc in self.descs:
            websites.append("offre-emploi.cm")
        return websites
  




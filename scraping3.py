from bs4 import BeautifulSoup
import requests

metiers = []
dates = []
entreprises = []
descriptions = []
regions = []
liens =[]
websites = []

class elements3:

    documents = requests.get("https://www.cameroondesks.com/").text
    soup = BeautifulSoup(documents, 'lxml')

    datas = soup.find_all('h2', class_='post-title')

    def metier(self):
        for data in self.datas:
            metiers.append(data.text)
        return metiers

    ##   print(metiers[i])

    def lien(self):
        for data in self.datas:
            liens.append(data.find('a').get('href'))
        return liens
    
    
    def taille(self):
        return len(self.lien())
  




    #for lien in liens:
    #   print(lien)

    donnees = soup.find_all('div', class_='resumo')

    def description(self):
        for donnee in self.donnees:
            descriptions.append(donnee.find('span').text)
        return descriptions

    def sites(self):
        for donnee in self.donnees:
            websites.append("cameroondesks.com")
        return websites



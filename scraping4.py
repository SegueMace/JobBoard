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

class Cote:

    documents = requests.get("https://www.emploi.ci/recherche-jobs-cote-ivoire").text
    soup = BeautifulSoup(documents, 'lxml')

    titles = soup.find_all('h5')

  
        
    #print(documents)


    datas = soup.find_all('p', class_='job-recruiter')

    
 

    descs = soup.find_all('div', class_='search-description')


    regs = soup.find_all('p', attrs={'class': None})



    a = soup.find_all('div', class_='job-description-wrapper') 
  

  


     

    def coteivoire(self):
        for reg in self.descs:
            descriptions.append(reg.text)
        for i in self.a:
            liens.append(i.get('data-href'))
        for title in self.titles:
            websites.append("emploi.ci")
        for title in self.titles:
            metiers.append(title.text)

          
        for i in range(len(liens)):
            values.append({'site':websites[i],'lien':liens[i], 'metier':metiers[i], 'description':descriptions[i]})
        return values




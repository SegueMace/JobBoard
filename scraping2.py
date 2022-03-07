from bs4 import BeautifulSoup
import requests

metiers = []
dates = []
entreprises = []
descriptions = []
regions = []
liens =[]

documents = requests.get("https://www.offre-emploi.cm/").text
soup = BeautifulSoup(documents, 'lxml')


datas = soup.find_all('div', class_='jobTitle')

for data in datas:
    metiers.append(data.text)

#for i in range(len(metiers)):
 #  print(metiers[i])



for data in datas:
    liens.append(data.find('a').get('href'))


for lien in liens:
    print(lien)



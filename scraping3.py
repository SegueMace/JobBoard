from bs4 import BeautifulSoup
import requests

metiers = []
dates = []
entreprises = []
descriptions = []
regions = []
liens =[]

documents = requests.get("https://www.cameroondesks.com/").text
soup = BeautifulSoup(documents, 'lxml')

datas = soup.find_all('h2', class_='post-title')

for data in datas:
    metiers.append(data.text)

##   print(metiers[i])

for data in datas:
    liens.append(data.find('a').get('href'))


#for lien in liens:
 #   print(lien)

donnees = soup.find_all('div', class_='resumo')

for donnee in donnees:
    descriptions.append(donnee.find('span').text)

for desc in descriptions:
    print(desc)
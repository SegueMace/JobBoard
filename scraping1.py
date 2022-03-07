from bs4 import BeautifulSoup
import requests

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

for entreprise in entreprises:
    print(entreprise)









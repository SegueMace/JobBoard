from bs4 import BeautifulSoup
import requests

metiers = []
dates = []
entreprises = []
descriptions = []
regions = []
liens =[]

def elements():

    documents = requests.get("https://www.emploi.cm/recherche-jobs-cameroun/").text
    soup = BeautifulSoup(documents, 'lxml')

    titles = soup.find_all('h5')

    for title in titles:
        metiers.append(title.text)



    #print(documents)


    datas = soup.find_all('p', class_='job-recruiter')

    for data in datas:
        dates.append((data.text).split('|')[0])


    for data in datas:
        entreprises.append((data.text).split('|')[1])


    descs = soup.find_all('div', class_='search-description')

    for desc in descs:
        descriptions.append(desc.text)

    regs = soup.find_all('p', attrs={'class': None})

    for reg in regs:
        regions.append(reg.text)


    a = soup.find_all('div', class_='job-description-wrapper')

    for i in a:
        liens.append(i.get('data-href'))




    #for i in range(len(metiers)):
    #   print(metiers[i])
    #  print(dates[i])
    # print(entreprises[i])
        #print(descriptions[i])
        #print(regions[i])
        #print(liens[i]) 


    #Fin de scraping pour emploi.cm
    for i in range(len(liens)):
      print(liens[i])


elements()
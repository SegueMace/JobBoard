from requests_html import HTMLSession

session = HTMLSession()

url = 'https://news.google.com/topstories?hl=fr&gl=FR&ceid=FR%3Afr'


r = session.get(url)

r.html.render(sleep=1, scrolldown=5)

articles = r.html.find('article')

#print(articles)

for item in articles:
    newsitem = item.find('h3', first=True)
    title = newsitem.text
    link = newsitem.absolute_links
    #print(title, link)


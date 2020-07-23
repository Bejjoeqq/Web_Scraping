from bs4 import BeautifulSoup as bs
import urllib3

http = urllib3.PoolManager()
url = 'https://pokemondb.net/pokedex/all'
response = http.request('GET', url).data.decode('utf-8')

soup = bs(response,features="html.parser")
tr = soup.find("table", class_ ="data-table").find("tbody").find_all("tr")
data=[]
for x in tr:
	td = x.find_all("td")
	temp=[]
	for y in range(len(td)):
		temp.append(td[y].get_text().replace("\n",""))
	data.append(temp)
for x in data:
	print(x)
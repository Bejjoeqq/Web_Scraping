from bs4 import BeautifulSoup as bs
import urllib3,pandas as pd

http = urllib3.PoolManager()
url = 'https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films'
response = http.request('GET', url).data.decode('utf-8')

soup = bs(response,features="html.parser")
data = soup.find_all("a")
result = []
for x in data:
	if "2019" in x:
		result.append(x.find_previous('a').get_text())
df = pd.DataFrame(data)
print(df)
from bs4 import BeautifulSoup as bs
import urllib3

http = urllib3.PoolManager()
url = 'https://blog.sanbercode.com/'
response = http.request('GET', url).data.decode('utf-8')

soup = bs(response,features="html.parser")
data = soup.find_all("div","mt-3 mt-md-0 mb-3 d-flex post_box_style3")

judul=[]
nama=[]

for x in data:
	judul.append(x.find("a","text-dark").get_text().replace("\n                ",""))
	nama.append(x.find("a","text-muted text-capitalize").get_text().replace("\n                    ",""))

for x in range(len(judul)):
	print(f"Judul : {judul[x]}\nPenulis : {nama[x]}\n")
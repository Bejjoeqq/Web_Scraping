from bs4 import BeautifulSoup as bs
import urllib3
# import pandas as pd

def getData(tr):
	data=[]
	for x in tr:
		td = x.find_all("td")
		temp=[]
		for y in range(len(td)):
			temp.append(td[y].get_text().replace("\n",""))
		data.append(temp)
	return data
def List_of_brightest_stars():
	http = urllib3.PoolManager()
	url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars'
	response = http.request('GET', url).data.decode('utf-8')

	soup = bs(response,features="html.parser")
	tr = soup.find("table", class_ ="sortable").find("tbody").find_all("tr")

	data = getData(tr)
	 
	data[1].insert(4, "")  
	rank=[];vm=[];pn=[];bd=[];part=[];dis=[];sc=[]
	for x in range(1,len(data)):
		rank.append(data[x][0])
		vm.append(data[x][1])
		pn.append(data[x][2])
		bd.append(data[x][3])
		part.append(data[x][4])
		dis.append(data[x][5])
		sc.append(data[x][6])


	data = {'Rank':rank,
	        'Visual magnitude':vm,
	        'Proper name':pn,
	        'Bayer design I':bd,
	        'Bayer design II':part,
	        'Distance':dis,
	        'Spectral class':sc}
	# df = pd.DataFrame(data)
	# display(df)
def List_of_action_films_of_the_2020s():
	http = urllib3.PoolManager()
	url = 'https://en.wikipedia.org/wiki/List_of_action_films_of_the_2020s'
	response = http.request('GET', url).data.decode('utf-8')

	soup = bs(response,features="html.parser")
	table = soup.find_all("table", class_ ="sortable")

	t2020 = table[0].find("tbody").find_all("tr")
	t2021 = table[1].find("tbody").find_all("tr")

	data1 = getData(t2020)
	data2 = getData(t2021)
	data = data1+data2

	for x in data:
		print(x)

def main():
	List_of_brightest_stars()
	List_of_action_films_of_the_2020s()
if __name__ == '__main__':
	main()
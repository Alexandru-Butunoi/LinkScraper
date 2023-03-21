
import requests
from bs4 import BeautifulSoup



def getting_data(url):
 	res = requests.get(url)
 	soup = BeautifulSoup(res.text, 'html.parser')
 	pages=[]
 	for link in soup.find_all('a'):
 		pages.append(link.get('href').replace('https://', ''))
 	return pages





from bs4 import BeautifulSoup
import requests
import time

pullDate = time.strftime("%Y-%m-%d")
url = 'https://data.sanantonio.gov/dataset/building-permits'

def getSoup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

soup = getSoup(url)
downloadLink = soup.find('a', {'class': 'resource-url-analytics'})['href']
permitsIssued = requests.get(downloadLink)

with open('data/{}.csv'.format(pullDate), 'wb') as f:
    f.write(permitsIssued.content)

print('Done!')
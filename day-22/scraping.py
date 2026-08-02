#Install request and beautifulsoup4 for scarping a website
pip install requests
pip install beautifulsoup4

#Scraping of a website is done here
#Website : Countries of the World: A Simple Example (scarpable sandbox which is available)
import requests
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/simple/'
response = requests.get(url)
status = response.status_code
print(status)
content = response.content
soup = BeautifulSoup(content,'html.parser')
print(soup.title)
print(soup.title.get_text())
print(soup.body)
print(response.status_code)
image = soup.find_all('img')  #returns all the img tags
print(image)  

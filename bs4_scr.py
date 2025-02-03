from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://gbenga.koyeb.app/contact'
page = urlopen(url)
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

print(soup.title.string)
# images = soup.find_all('img')
# for image in images:
#     print(image['src'])
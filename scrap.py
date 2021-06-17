from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "{insertURLhere}"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

data = soup.find_all('{insertTAGhere}', class_='{insertCLASShere}')
print(data)

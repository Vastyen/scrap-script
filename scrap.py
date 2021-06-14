from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "{insertURLhere}"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

eq = soup.find_all('{insertTAGhere', class_='insertCLASShere')
print(eq)

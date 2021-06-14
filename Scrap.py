from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://chile.as.com/resultados/futbol/chile/clasificacion/"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#Equipos

eq = soup.find_all('span', class_='nombre-equipo')
print(eq)

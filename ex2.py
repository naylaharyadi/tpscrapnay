import requests
from bs4 import BeautifulSoup

# Liste des URLs des pages à scraper
urls = [
    'https://www.scrapethissite.com/pages/forms/',
    'https://www.scrapethissite.com/pages/forms/?page_num=2', 'https://www.scrapethissite.com/pages/forms/?page_num=3', 'https://www.scrapethissite.com/pages/forms/?page_num=4', 'https://www.scrapethissite.com/pages/forms/?page_num=5', 'https://www.scrapethissite.com/pages/forms/?page_num=6', 'https://www.scrapethissite.com/pages/forms/?page_num=7', 'https://www.scrapethissite.com/pages/forms/?page_num=8', 'https://www.scrapethissite.com/pages/forms/?page_num=9', 'https://www.scrapethissite.com/pages/forms/?page_num=10'
]

# Liste pour stocker les données extraites de toutes les pages
all_data = []

for url in urls:
    # Envoyer la requête HTTP pour obtenir le contenu de la page
    response = requests.get(url)

    # Analyser le contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Trouver tous les éléments souhaités (exemple avec des titres)
    teams = soup.find_all (class_='name') 

    # Extraire les données de chaque titre et les stocker
    page_data = [team.text.strip() for team in teams]
    all_data.append(page_data)

# Afficher les données extraites de chaque page
for data in all_data:
    for item in data:
        print(item) 

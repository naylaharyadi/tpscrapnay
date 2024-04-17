#pour afficher les pays et les capitales :
import requests
from bs4 import BeautifulSoup


#URL = 'https://www.scrapethissite.com/pages/simple/'
#s = requests.Session()
#r=s.get(URL)

#soup = BeautifulSoup (r.text, 'html.parser') 

#data = soup.find_all('table')[0]

#df = pd.read_html(str(data))[0] 


# Faire la requête HTTP
url = "https://www.scrapethissite.com/pages/simple/"
r = requests.get(url)
# Vérifier si la requête a réussi
if r.status_code == 200:
    # Analyser le contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(r.text, 'html.parser')
    # Trouver tous les éléments qui contiennent les noms des pays
    country_elements = soup.find_all(class_='country-name')
    # Trouver tous les éléments qui contiennent les capitales
    capital_elements = soup.find_all(class_='country-capital')
    # Récupérer les noms des pays
    countries = [element.get_text(strip=True) for element in country_elements]
    # Récupérer les capitales
    capitals = [element.get_text(strip=True) for element in capital_elements]
    # Afficher les pays et leurs capitales respectives
    for country, capital in zip(countries, capitals):
        print(f"{country} - {capital}")
else:
    print("La requête a échoué avec le code :", r.status_code) 
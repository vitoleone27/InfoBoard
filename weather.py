
from bs4 import BeautifulSoup
import requests

contents = requests.get('http://forecast.weather.gov/MapClick.php?lat=40.6222&lon=-75.3932')
soup = BeautifulSoup(contents.text, 'html.parser')

forecasts = soup.find_all('img', class_='forecast-icon')

locations = soup.find('div', class_='panel panel-default').find_next_sibling('div')
locations = locations.find('h2', class_='panel-title')

print(locations.string)

for forecast in forecasts:
    print(forecast['alt'])

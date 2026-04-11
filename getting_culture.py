import json
import requests
import os
from dotenv import load_dotenv
import pyeuropeana.apis as apis
import py_cartes_io as cartes

# API key stuff
load_dotenv()
api_key = os.getenv("X-CSCAPI-KEY")

# Making Call to the CSC API
def get_cities_by_state(country_code, state_code):
    response = requests.get(
      f'https://api.countrystatecity.in/v1/countries/{country_code}/states/{state_code}/cities',
      headers={'X-CSCAPI-KEY': api_key}
    )
    
    if response.ok:
        cities = response.json()
        print(f'Found {len(cities)} cities in {state_code}, {country_code}')
        return cities
    else:
        print('State not found or no cities available')
        return []

cities = get_cities_by_state('US', 'IL')
print(cities)

# Making call to the Europeana API
europeana_api_key = os.getenv("EUROPEANA_API_KEY")
os.environ['EUROPEANA_API_KEY'] = europeana_api_key

response_europeana = apis.search(
    query="Champaign-Urbana",
    qf="TYPE:TEXT",
    reusability="open AND permission",
    media=True,
    thumbnail=True,
    landingpage=True,
    rows=100
)
print("\nFull Europeana response for the query:")
print(response_europeana.get('items', [])[1:])

with open("api-getting-data/getting_culture_results.json", "wt", encoding="utf-8") as outfile:
    outfile.write(json.dumps({ 
        "cities": cities, 
        "europeana": response_europeana
    }, indent = 2))
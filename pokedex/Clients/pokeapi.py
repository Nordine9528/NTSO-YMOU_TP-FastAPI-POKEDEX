import requests
from database import database

def get_pokemon_from_api(pokemon_id: int):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    print(f"\ncode status requete pokeapi : {response.status_code}")
    response_json = response.json()
    try:
        database.db_insert_pokemon(response_json)
    except Exception as e:
        print(f"Erreur lors de l'insertion dans la db: {e}")

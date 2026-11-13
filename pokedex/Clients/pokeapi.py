import requests
from database import database

def get_pokemon_from_api(pokemon_id: int):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    response_json = response.json()
    return response_json

def get_pokemon_fr_name(pokemon_id: int):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}")
    response_json = response.json()
    if (response_json['names'][4]['language']['name'] == "fr"):
        name = response_json['names'][4]['name']
    else :
        name = response_json['names']
    return name
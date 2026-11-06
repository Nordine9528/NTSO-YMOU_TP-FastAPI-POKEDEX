import requests
import fastapi
from schemas.pokemon import Pokemon
from database import database

app = fastapi.FastAPI()

database.init_connection_db()
database.init_connection_db_show_tables()

@app.get("/health")
def GET_health():
    return {"status": "ok"}

@app.get("/pokemon/{pokemon_id}")
def get_pokemon(pokemon_id: int):
    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    except Exception as e:
        print(e)

    if(response.status_code == 200):
        return response.json()
    else:
        return response.status_code

@app.post("/pokemons/{pokemon_id}/scan")
def scan_pokemon(pokemon_id: int):
    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
        response.json()
    except Exception as e:
        print(e)
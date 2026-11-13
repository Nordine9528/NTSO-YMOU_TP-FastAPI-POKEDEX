import fastapi
from schemas.pokemon import Pokemon
from Clients import pokeapi as f_pokapi
from database import database

app = fastapi.FastAPI()

database.init_connection_db()
database.init_connection_db_show_tables()

@app.get("/health")
def GET_health():
    return {"status": "ok"}

@app.get("/pokemons/{pokemon_id}/scan")
def get_pokemon(pokemon_id: int):
    f_pokapi.get_pokemon_from_api(pokemon_id)
    print("bonjour")




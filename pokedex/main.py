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
    r_json = f_pokapi.get_pokemon_from_api(pokemon_id)
    name_fr = f_pokapi.get_pokemon_fr_name(pokemon_id)

    database.db_insert_pokemon(r_json, name_fr)




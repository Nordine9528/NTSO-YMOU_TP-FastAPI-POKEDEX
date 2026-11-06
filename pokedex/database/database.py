import sqlite3

def init_connection_db():
    connection = sqlite3.connect("pokedex.db")
    cursor = connection.cursor()
    cursor.execute("""
     CREATE TABLE IF NOT EXISTS pokemon (
     number INTEGER PRIMARY KEY,
     name TEXT NOT NULL,
     name_fr TEXT NOT NULL,
     types TEXT NOT NULL,
     image_url TEXT NOT NULL,
     height INTEGER NOT NULL,
     weight INTEGER NOT NULL,
     evolves_from_number INTEGER
     )
    """)
    connection.commit()
    connection.close()
    print("Base de données creee avec succes.")

def init_connection_db_show_tables():
    connection = sqlite3.connect("pokedex.db")
    cursor = connection.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
    tables = cursor.fetchall()

    print("Voici les tables :\n")
    print([t[0] for t in tables])
    connection.close()

def db_insert_pokemon(pokemon_json):
    if (len(pokemon_json['types']) < 2):
        types = pokemon_json['types'][1]['type']['name']
    else:
        types = pokemon_json['types'][0]['type']['name'] + pokemon_json['types'][1]['type']['name']

    connection = sqlite3.connect("pokedex.db")
    cursor = connection.cursor()
    connection.execute(
        "INSERT OR REPLACE INTO pokemon VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (
            pokemon_json["id"],
            pokemon_json["name"],
            pokemon_json["name"],
            types,
            pokemon_json["sprites"]["front_default"],
            pokemon_json["height"],
            pokemon_json["weight"],
            None,
        ),
    )
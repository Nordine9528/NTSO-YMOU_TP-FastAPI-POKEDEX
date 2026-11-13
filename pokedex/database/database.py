import sqlite3

from numpy import char

from schemas import pokemon


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

    print([t[0] for t in tables])
    connection.close()

def db_insert_pokemon(pokemon_json : pokemon, pokemon_name_fr : char):
    if (len(pokemon_json['types']) < 2):
        types = f"{pokemon_json['types'][0]['type']['name']}"
    else:
        types = f"{pokemon_json['types'][0]['type']['name']}; {pokemon_json['types'][1]['type']['name']}"

    print("je suis ici apres la detection du type\n")
    Poid_pokemon = pokemon_json["weight"] / 10
    Taille_pokemon = pokemon_json["height"] / 10

    print(f"Poids {Poid_pokemon}, Taille {Taille_pokemon}")

    connection = sqlite3.connect("pokedex.db")
    cursor = connection.cursor()

    cursor.execute(
        "INSERT OR REPLACE INTO pokemon VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (
            pokemon_json["id"],
            pokemon_json["name"].capitalize(),
            pokemon_name_fr.capitalize(),
            types.capitalize(),
            pokemon_json["sprites"]["front_default"],
            Taille_pokemon,
            Poid_pokemon,
            None,
        ),
    )
    if cursor.rowcount == 0:
        print(f"Pokemon {pokemon_json['name']} (id : {pokemon_json['id']}) deja dans la table")
    else:
        print(f"Pokemon {pokemon_json['name']} (id : {pokemon_json['id']}) ajoute dans la table")

    connection.commit()
    connection.close()

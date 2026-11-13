import requests
import json

url = "http://127.0.0.1:8000/pokemons/25/scan"
r = requests.get(url)
print(r.status_code)



''' 
print(f"Numero : {req_json['id']}")
print(f"Nom : {req_json['name']}")
print(f"Type 1 : {req_json['types'][0]['type']['name']}")
types = req_json['types']
print( types)


if (len(req_json['types'])<2):
    print("Pas de second type")
else :
    print(f"Type 2 : {req_json['types'][1]['type']['name']}")

print(f"Hauteur : {req_json['height']}")
print(f"Poids : {req_json['weight']}")
'''




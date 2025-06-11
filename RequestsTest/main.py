import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8ad291f607042f6a51243046327d979b'
HEADER = {'Content-Type': 'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "Вольт",
    "photo_id": 12
}

body_change = {
    "pokemon_id": "334624",
    "name": "Коламбус",
    "photo_id": 2
}

body_catch = {
    "pokemon_id": "334624"
}



'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''


'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''


response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)
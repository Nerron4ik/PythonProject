import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8ad291f607042f6a51243046327d979b'
HEADER = {'Content-Type': 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '34006'


def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params= {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200
    
def test_trainer_name():
    response = requests.get(url = f'{URL}/trainers/34006', params= {'trainer_id' : TRAINER_ID})
    assert response.json()['trainer_name'] == 'Ричер'
import os
import random
import requests

try:
    ENV_SECRET = os.environ["SECRET"]
except KeyError:
    ENV_SECRET = "¡Secret no existe!"


if __name__ == "__main__":
    print(f"Valor del Secret: {ENV_SECRET}")

    r = requests.get('https://rickandmortyapi.com/api/character')
    number = random.randint(1, 20)
    if r.status_code == 200:
        data = r.json()
        name = data["results"][number]["name"]
        print(f'Consulta a la API de Rick y Morty...')
        print(f'Tu personaje es: {name}')
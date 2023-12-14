from fastapi import FastAPI
import json

with open('./perso.json', 'r', encoding='utf-8') as jsonfile:
    perso = json.load(jsonfile)
    
print(perso['name'])

app = FastAPI()

@app.get('/test_perso')
async def test_perso():
    return perso
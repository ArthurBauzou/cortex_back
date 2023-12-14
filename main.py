from fastapi import FastAPI
from db.database import testread

app = FastAPI()

@app.get('/')
async def home():
    return('nope')

@app.get('/test')
async def test():
    blankman = testread()
    print(blankman['name'])
    return blankman
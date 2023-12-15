from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.database import testread

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def home():
    return('nope')

@app.get('/test')
async def test():
    blankman = testread()
    # print(blankman['name'])
    return blankman
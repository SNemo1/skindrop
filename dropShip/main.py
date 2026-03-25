import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

skins = [
    {'name' : 'Awp Asimov', 'sum' : 15000 , 'procent' : 5.4},
    {'name' : 'AK47 Neon-Rider', 'sum' : 1000 , 'procent' : 24.6},
    {'name' : 'Awp Neo-Nuar', 'sum' : 5000 , 'procent' : 30},
    {'name' : 'glock Shinobu' ,'sum' : 500 , 'procent' : 40}
]

@app.get("/spin")
def spin_roulette():
    chances = [5.4, 24.6, 30, 40]
    winner = random.choices(skins, k = 1, weights = chances)

    return {"massage": f"Оце так пощастило! Тобі випав {winner[0]['name']} {winner[0]['sum']}"}
import random

skins = [
    {'name' : 'Awp Asimov', 'sum' : 15000 , 'procent' : 5.4},
    {'name' : 'AK47 Neon-Rider', 'sum' : 1000 , 'procent' : 24.6},
    {'name' : 'Awp Neo-Nuar', 'sum' : 5000 , 'procent' : 30},
     {'name' : 'glock Shinobu' ,'sum' : 500 , 'procent' : 40}
]


def spin_roulette(skins_list):
    chances = [5.4, 24.6, 30, 40]
    winner = random.choices(skins_list, k = 1, weights = chances)

    print(f"Оце так пощастило! Тобі випав {winner[0]['name']} {winner[0]['sum']}")

spin_roulette(skins)
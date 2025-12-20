from game.logic import create_players

names = ["Ярік", "Остап", "Павло", "Бот1", "Бот2"]

players = create_players(names)

for p in players:
    print(p)

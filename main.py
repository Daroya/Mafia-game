from game.state import Player
from game.roles import Mafia, Doctor, Civilian, Sheriff
from game.logic import night, day

# створюємо гравців це дньои зробив щас буду робити всьо для шерифа і ось боти чекай
players = [
    Player("Ярослав", Mafia()),
    Player("Остап", Doctor()),
    Player("Павло", Civilian()),
    Player("Бот1", Civilian()),
    Player("Бот2", Sheriff()) 
]

#Тест гри в консолі на ботах
def check_win(players):
    mafia_alive = 0
    civilians_alive = 0

    for p in players:
        if p.alive == True:
            if isinstance(p.role, Mafia):
                mafia_alive += 1
            else:
                civilians_alive += 1

    if mafia_alive == 0:
        print("Мирні перемогли!")
        return True

    if mafia_alive >= civilians_alive:
        print("Мафія перемогла!")
        return True

    return False


print("Гра почалась!")

while True:
    night(players)

    if check_win(players):
        break

    day(players)

    if check_win(players):
        break

from game.state import Player
from game.roles import Mafia, Doctor, Civilian, Sheriff
from game.logic import night, day, end_game

players = [
    Player("Ярослав", Mafia()),
    Player("Остап", Doctor()),
    Player("Павло", Civilian()),
    Player("Бот1", Civilian()),
    Player("Бот2", Sheriff())
]

def check_win(players):
    mafia = 0
    civilians = 0

    for p in players:
        if p.alive:
            if isinstance(p.role, Mafia):
                mafia += 1
            else:
                civilians += 1

    if mafia == 0:
        print("🎉 Мирні перемогли!")
        return True

    if mafia >= civilians:
        print("💀 Мафія перемогла!")
        return True

    return False

print("Гра почалась!")

day_count = 1

while not check_win(players):

    print(f"\n🌙 НІЧ {day_count}")
    night(players)

    if check_win(players):
        break

    print(f"\n☀️ ДЕНЬ {day_count}")
    day(players)

    day_count += 1

print("\n=== ГРА ЗАКІНЧИЛАСЬ ===")
end_game(players)


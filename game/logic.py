import random
from game.roles import Mafia, Doctor, Civilian, Sheriff
from game.state import Player

def create_players(names):
    roles = [
        Mafia(),
        Doctor(),
        Sheriff()
    ]

    while len(roles) < len(names):
        roles.append(Civilian())

    random.shuffle(roles)

    players = []
    for i in range(len(names)):
        players.append(Player(names[i], roles[i]))

    return players

def night(players):
    night_has_comeprint = ("Настала ніч")

    alive_players = []

    # 1. збираємо живих
    for p in players:
        if p.alive == True:
            alive_players.append(p)

    # 2. шукаємо мафію
    mafia_players = []
    for p in alive_players:
        if isinstance(p.role, Mafia):
            mafia_players.append(p)

    if len(mafia_players) == 0:
        return

    # 3. мафія вибирає жертву
    victim = random.choice(alive_players)

    # 4. шукаємо лікаря
    doctors = []
    for p in alive_players:
        if isinstance(p.role, Doctor):
            doctors.append(p)

    healed = None
    if len(doctors) > 0:
        healed = random.choice(alive_players)

    if victim != healed:
        victim.kill()


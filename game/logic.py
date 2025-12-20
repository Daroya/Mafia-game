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

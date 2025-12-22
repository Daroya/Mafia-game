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
    print("Настала ніч!")

    alive_players = []
    for p in players:
        if p.alive:
            alive_players.append(p)

    # мафія
    mafia_players = []
    for p in alive_players:
        if isinstance(p.role, Mafia):
            mafia_players.append(p)

    if len(mafia_players) == 0:
        return
    
    victim = random.choice(alive_players)

    while isinstance(victim.role, Mafia):
        print("Ніч: Мафія не може вбити себе")
        victim = random.choice(alive_players)

    # лікар
    doctors = []
    for p in alive_players:
        if isinstance(p.role, Doctor):
            doctors.append(p)
    print('Ніч: Лікар вийшов на зміну')

    healed = None
    if len(doctors) > 0:
        healed = random.choice(alive_players)

    # мафія вбила
    if victim != healed:
        victim.kill()
        print("Ніч: мафія вбила", victim.name)
    else:
        print("Ніч: лікар врятував гравця")

    alive_players = []
    for p in players:
        if p.alive:
            alive_players.append(p)

    # шериф
    sheriffs = []
    for p in alive_players:
        if isinstance(p.role, Sheriff):
            sheriffs.append(p)

    if len(sheriffs) > 0 and len(alive_players) > 1:
        checked = random.choice(alive_players)
        print(f"Ніч: шериф перевірив {checked.name}")


#логика дня
def day(players):
    print("Настав день!")

    alive_players = []
    for p in players:
        if p.alive:
            alive_players.append(p)
    #
    voted_player = random.choice(alive_players)
    voted_player.kill()

    print("День: вигнали", voted_player.name)

#
def end_game(players):
    print("\nРолі гравців:")
    for p in players:
        status = "живий" if p.alive else "мертвий"
        print(f"{p.name} — {p.role.name} — {status}")

    

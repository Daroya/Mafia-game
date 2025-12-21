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

    # 1. збираємо живих
    for pn in players:
        if pn.alive == True:
            alive_players.append(pn)

    #Логіка мафії
    mafia_players = []
    for pn in alive_players:
        if isinstance(pn.role, Mafia):
            mafia_players.append(pn)

    if len(mafia_players) == 0:
        return

    # мафія вибирає жертву
    victim = random.choice(alive_players)

    #Логіка лікаря
    doctors = []
    for pn in alive_players:
        if isinstance(pn.role, Doctor):
            doctors.append(pn)

    healed = None
    if len(doctors) > 0:
        healed = random.choice(alive_players)

    if victim != healed:
        victim.kill()
        print(f"Вночі загинув: {victim.name}")
    
    #Логіка Ширіфа
    sheriff = []
    for pn in alive_players:
        if isinstance(pn.role, Sheriff):
            sheriff.append(pn)
    #Рандом вибір кого вбити ширіфа
    sheriff_victim = random.choice(alive_players)
    if victim == sheriff:
        sheriff.kill()
    else:
        sheriff_victim.kill()
    print(f'Сьогодні Шериф убив {sheriff_victim.name}')

#логика дня
def day(players):
    print("Настав день!")

    alive_players = []
#Провірка чи живий гравець і чи може він голосуати
    for pd in players:
        if pd.alive == True:
            alive_players.append(pd)
#Рандом голосованіє
    voted_player = random.choice(alive_players)
#Вибити людей за яких голосували
    if voted_player.alive == True:
        voted_player.kill()
    print(f"Вигнали гравця: {voted_player.name}")

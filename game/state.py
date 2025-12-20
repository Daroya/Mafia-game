class Player:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.alive = True

    def kill(self):
        self.alive = False

    def __str__(self):
        status = "Живий" if self.alive else "Мертвий"
        return f"{self.name} ({self.role.name}) - {status}"

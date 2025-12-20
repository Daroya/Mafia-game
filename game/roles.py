class Role:
    def __init__(self, name):
        self.name = name

class Mafia(Role):
    def __init__(self):
        super().__init__("Mafia")

class Doctor(Role):
    def __init__(self):
        super().__init__("Doctor")

class Civilian(Role):
    def __init__(self):
        super().__init__("Civilian")

class Sheriff(Role):
    def __init__(self):
        super().__init__('Sheriff')
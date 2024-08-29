class Person:
    def __init__(self, name, hp, damage):
        if hp > 0 and damage > 0:
            self.name = name
            self._hp = hp
            self.damage = damage
        else:
            raise ValueError("hp and damage must be a positive number.")
    
    @property
    def hp(self):
        return self._hp
    
    @hp.setter
    def hp(self, value):
        self._hp = value

        if self._hp < 0:
            self._hp = 0
    
    def hit(self, who):
        self.hp -= who.damage
    
    def alive(self):
        return self.hp > 0

class Marvel:

    def __init__(self, name, health, attackPower, armorNumber):
        self.name = name
        self.health = health
        self.attackpower = attackPower
        self.armorNumber= armorNumber

def serang(self, lawan):
    print(self.name + " menyerang " + lawan.name)
    lawan.diserang(self, self.attackPower)

def diserang(self, lawan, attackPower)
class Marvel:
    # class variabel
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor= inputArmor
        Marvel.jumlah += 1
        print("Hero Marvel dengan nama : " + inputName)

marvel1 = Marvel("Iron Man",1000,900,800)
print(Marvel.jumlah)
maervel2 = Marvel("Thor",900,1000,900)
print(Marvel.jimlah)
marvel3 = Marvel("Captain America",800,700,600)
print(Marvel.jumlah)
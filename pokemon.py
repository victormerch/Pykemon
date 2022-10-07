class Pokemon:
    # Constructor de la clase Pokemon.
    def __init__(self, name, type, hp, ataques,imgFront, imgBack):
        self.name = name
        self.type = type
        self.hp = hp
        self.ataques = ataques
        self.imgFront = imgFront
        self.imgBack = imgBack
    
    #Getters
    def getName(self):
        return self.name
    def getType(self):
        return self.type
    def getAtaques(self):
        return self.ataques
    def getImgFront(self):
        return self.imgFront
    def getImgBack(self):
        return self.imgBack
    def getHp(self):
        return self.hp
    
    #Setters
    def setName(self, name):
        self.name = name
    def setType(self, type):
        self.type = type
    def setAtaques(self, ataques):
        self.ataques = ataques
    def setImgFront(self, imgFront):
        self.imgFront = imgFront
    def setImBack(self, imgBack):
        self.imgBack = imgBack
    def setHp(self, hp):
        self.hp = hp
        
class Ataque():
    
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
        
    def getDamage(self):
        return self.damage
    def getName(self):
        return self.name
    
    def setDamage(self, damage):
        self.damage = damage
    def setName(self, name):
        self.name = name
        
    
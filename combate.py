class Combate:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.turno = 0
        self.pokemon1.setHp(100)
        self.pokemon2.setHp(100)
        
    
    def ronda(self, ataqueUser, ataqueBot):
        texto = ["","",""]
        #Ataque del usuario
        self.pokemon2.setHp(self.pokemon2.getHp()-ataqueUser.getDamage())
        #Ataque del bot
        self.pokemon1.setHp(self.pokemon1.getHp()-ataqueBot.getDamage())

        texto[0] = self.pokemon1.getName() + " uso " + ataqueUser.getName()
        texto[1] = self.pokemon2.getName() + " uso " + ataqueBot.getName() 
        
        
        if self.pokemon1.getHp() <= 0 and self.pokemon2.getHp() <= 0:
            self.pokemon1.setHp(0)
            self.pokemon2.setHp(0)
            texto[2] = "==EMPATE=="
        else:
            #Si el pokemon del usuario muere
            if self.pokemon1.getHp() <= 0:
                self.pokemon1.setHp(0)
                texto[2] = "==HAS PERDIDO=="
                
            #Si el pokemon del bot muere
            if self.pokemon2.getHp() <= 0:
                self.pokemon2.setHp(0)
                texto[2] = "==HAS GANADO LA PARTIDA=="
            
               
    
        return texto 
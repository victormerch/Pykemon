# Importar e inicializar Pygame.
import re
import pygame
import random

class Pokemon:
    # Constructor de la clase Pokemon.
    def __init__(self, name, type, imgFront, imgBack):
        self.name = name
        self.type = type
        self.imgFront = imgFront
        self.imgBack = imgBack
    
    #Getters
    def getType(self):
        return self.type
    def getImgFront(self):
        return self.imgFront
    def getImgBack(self):
        return self.imgBack
    #Setters
    def setType(self, type):
        self.type = type
    def setImgFront(self, imgFront):
        self.imgFront = imgFront
    def setImBack(self, imgBack):
        self.imgBack = imgBack
        
    def __str__(self):
        return self.name

pokemons = [Pokemon("Charmander", "Fuego", "Images/Sprites/4_charmander_front.png", "Images/Sprites/4_charmander_back.png"),
             Pokemon("Squirtle", "Agua", "Images/Sprites/7_squirtle_front.png", "Images/Sprites/7_squirtle_back.png"),
             Pokemon("Bulbasaur", "Planta", "Images/Sprites/1_bulbasaur_front.png", "Images/Sprites/1_bulbasaur_back.png")]
    
pygame.init()

# Crear la ventana y poner el tamaño.
screen = pygame.display.set_mode((400, 630))
bg = pygame.image.load("Images/bg1.png")
# Poner el título de la ventana.

#Background
pygame.display.set_caption("Pykemon")
screen.blit(bg, (0, 0))
#Texto de escoje tu pokemon
font = pygame.font.Font('Fonts/pokemon_generation_1.ttf', 12)
text = font.render('Pulsa para emepzar...', True,(250,250,250))
screen.blit(text,(220,580))
#Icon of the game
programIcon = pygame.image.load('Images/icon.png')
pygame.display.set_icon(programIcon)

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
 

clock = pygame.time.Clock()
salir = False
pantalla2 = False
pantalla3 = False

# Loop principal (game loop) del juego.
while not salir:

    # Timer que controla el frame rate.
    clock.tick(60)

    # Procesar los eventos que llegan a la aplicación.
    for event in pygame.event.get():
        
        # Si se cierra la ventana se sale del programa.
        if event.type == pygame.QUIT:
            salir = True

        # Si se pulsa la tecla [Esc] se sale del programa.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                salir = True
            else:
                pantalla2 = True
                
        if pantalla2: 
            
            #PANEL DE ELECION DE POKEMON
            #Cambiamos el color de fondo
            screen.fill([235, 240, 186])
            #Añadimos los pokemons
            pokemon1 = pygame.image.load(pokemons[0].getImgFront()).convert_alpha()
            pokemon2 = pygame.image.load(pokemons[1].getImgFront()).convert_alpha()
            pokemon3 = pygame.image.load(pokemons[2].getImgFront()).convert_alpha()
            screen.blit(pygame.transform.scale(pokemon1, (100, 100)), (60, 320))
            screen.blit(pygame.transform.scale(pokemon2, (100, 100)), (250, 320))
            screen.blit(pygame.transform.scale(pokemon3, (100, 100)), (147, 460))
            #Texto de escoje tu pokemon
            text = font.render('Escoje tu Pokemon ...', True,(0,0,0))
            font = pygame.font.Font('Fonts/pokemon_generation_1.ttf', 18)
            screen.blit(text,(65,180))   
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if pygame.Rect(60, 320, 100, 100).collidepoint(x, y):
                        pantalla2 = False
                        pantalla3 = True
                        
                        pokemonUser = pokemons[0]
                        pokemonBot = random.choice(pokemons)
                        bgs = ["background_1.png","background_2.png","background_3.png","background_4.png"]
                        bgEscenario = random.choice(bgs)
                    elif pygame.Rect(250, 320, 100, 100).collidepoint(x, y):
                        pantalla2 = False
                        pantalla3 = True
                        
                        pokemonUser = pokemons[1]
                        pokemonBot = random.choice(pokemons)
                        bgs = ["background_1.png","background_2.png","background_3.png","background_4.png"]
                        bgEscenario = random.choice(bgs)
                    elif pygame.Rect(147, 460, 100, 100).collidepoint(x, y):
                        pantalla2 = False
                        pantalla3 = True
                        
                        pokemonUser = pokemons[2]
                        pokemonBot = random.choice(pokemons)
                        bgs = ["background_1.png","background_2.png","background_3.png","background_4.png"]
                        bgEscenario = random.choice(bgs)
        if pantalla3:   
            #PANEL DE BATALLA
            screen.fill([235, 240, 186])
            
            #Escenario
            escenario = pygame.image.load("Images/Backgrounds/"+bgEscenario).convert_alpha()
            screen.blit(pygame.transform.scale(escenario, (350, 250)), (25, 20))
            #pokemons
            pokemon1 = pygame.image.load(pokemonUser.getImgBack()).convert_alpha()
            screen.blit(pygame.transform.scale(pokemon1, (100, 100)), (30, 160))
            
            pokemon2 = pygame.image.load(pokemonBot.getImgFront()).convert_alpha()
            screen.blit(pygame.transform.scale(pokemon2, (100, 100)), (230, 70))
        
                
                
    # Actualizar la pantalla.
    pygame.display.flip()
    pygame.display.update()

# Cerrar Pygame y liberar los recursos que pidió el programa.
pygame.quit()

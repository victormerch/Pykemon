# Importar e inicializar Pygame.
import re
import pygame
import random
from pokemons import *


pokemons = [Pokemon("Charmander", "Fuego",150,[Ataque("Scratch",30),Ataque("Growl",40),Ataque("Ember",25),Ataque("Smokescreen",20)], "Images/Sprites/4_charmander_front.png", "Images/Sprites/4_charmander_back.png"),
             Pokemon("Squirtle", "Agua",150,[Ataque("Headbutt",45),Ataque("Tackle",40),Ataque("Strength",20),Ataque("Skull Bash",10)], "Images/Sprites/7_squirtle_front.png", "Images/Sprites/7_squirtle_back.png"),
             Pokemon("Bulbasaur", "Planta",180,[Ataque("Cut",30),Ataque("Bind",15),Ataque("Headbutt",40),Ataque("Tackle",35)], "Images/Sprites/1_bulbasaur_front.png", "Images/Sprites/1_bulbasaur_back.png")]
bgs = ["background_1.png","background_2.png","background_3.png","background_4.png","background_5.png","background_6.png","background_7.png",
       "background_8.png","background_9.png","background_10.png","background_11.png"]
  
pygame.init()

# Crear la ventana y poner el tamaño.
screen = pygame.display.set_mode((400, 630))
bg = pygame.image.load("Images/bg1.png")
# Poner el título de la ventana.

#Background
pygame.display.set_caption("Pykemon")
screen.blit(bg, (0, 0))
#Texto de escoje tu pokemon
font = pygame.font.Font('Fonts/pokemon_generation_1.ttf', 11)
text = font.render('Pulsa para emepzar...', True,(250,250,250))
screen.blit(text,(230,580))
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
            font = pygame.font.Font('Fonts/pokemon_generation_1.ttf', 18)
            text = font.render('Escoje tu Pokemon ...', True,(0,0,0))
            screen.blit(text,(65,180))   
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if pygame.Rect(60, 320, 100, 100).collidepoint(x, y):
                        pantalla2 = False
                        pantalla3 = True
                        
                        pokemonUser = pokemons[0]
                        pokemonBot = random.choice(pokemons)
                        bgEscenario = random.choice(bgs)
                    elif pygame.Rect(250, 320, 100, 100).collidepoint(x, y):
                        pantalla2 = False
                        pantalla3 = True
                        
                        pokemonUser = pokemons[1]
                        pokemonBot = random.choice(pokemons)
                        bgEscenario = random.choice(bgs)
                    elif pygame.Rect(147, 460, 100, 100).collidepoint(x, y):
                        pantalla2 = False
                        pantalla3 = True
                        
                        pokemonUser = pokemons[2]
                        pokemonBot = random.choice(pokemons)
                        bgEscenario = random.choice(bgs)
        if pantalla3:   
            #PANEL DE BATALLA
            screen.fill([235,240,186])
            
            #Escenario
            escenario = pygame.image.load("Images/Backgrounds/"+bgEscenario).convert_alpha()
            screen.blit(pygame.transform.scale(escenario, (350, 250)), (25, 20))
            pygame.draw.rect(screen, (0,0,0), (25,20,350,250),  2, 3)#Borde
            #pokemons
            pokemon1 = pygame.image.load(pokemonUser.getImgBack()).convert_alpha()
            screen.blit(pygame.transform.scale(pokemon1, (100, 100)), (30, 160))
            
            pokemon2 = pygame.image.load(pokemonBot.getImgFront()).convert_alpha()
            screen.blit(pygame.transform.scale(pokemon2, (100, 100)), (230, 70))
            
            #Nombre con hp
            font = pygame.font.Font('Fonts/pokemon_generation_1.ttf', 12)
            nameHp1 = pokemonBot.getName().upper()+": "+str(pokemonBot.getHp())
            text1 = font.render(nameHp1, True,(0,0,0))
            
            screen.blit(text1,(30,40)) 
            
            nameHp2 = pokemonUser.getName().upper()+": "+str(pokemonUser.getHp())
            text2 = font.render(nameHp2, True,(0,0,0))
            
            screen.blit(text2,(220,230)) 
        
            #TextArea del terminal
            pygame.draw.rect(screen, (0,0,0), (25,280,350,110),  2, 3)
            
            #Botones de ataques
            #for i in range(4):
            pygame.draw.rect(screen, (0,0,0), (25,395,170,100),  2, 3)
            pygame.draw.rect(screen, (0,0,0), (205,395,170,100),  2, 3)
            pygame.draw.rect(screen, (0,0,0), (25,500,170,100),  2, 3)
            pygame.draw.rect(screen, (0,0,0), (205,500,170,100),  2, 3)
            
            font = pygame.font.Font('Fonts/pokemon_generation_1.ttf', 20)
            
            text1 = font.render(pokemonUser.getAtaques()[0].getName(), True,(0,0,0))
            screen.blit(text1,(50,410)) 
            
            text2 = font.render(pokemonUser.getAtaques()[1].getName(), True,(0,0,0))
            
            screen.blit(text2,(230,410)) 
            
            text3 = font.render(pokemonUser.getAtaques()[2].getName(), True,(0,0,0))
            screen.blit(text3,(50,510)) 
            
            text4 = font.render(pokemonUser.getAtaques()[3].getName(), True,(0,0,0))
            
            screen.blit(text4,(230,510)) 
        
                
                
    # Actualizar la pantalla.
    pygame.display.flip()
    pygame.display.update()

# Cerrar Pygame y liberar los recursos que pidió el programa.
pygame.quit()

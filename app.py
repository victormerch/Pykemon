"""
TAREAS:
- Crear classes para las pantallas
- Crear funciones para absolutamente todo
- Optimizar codigo
- Arreglar problema de las dependencias de la env del proyecto
"""


# Importar e inicializar Pygame
from pathlib import Path
import pygame
import random
from pokemon import *
from combate import Combate
from tkinter import messagebox 


bgs = ["background_1.png","background_2.png","background_3.png","background_5.png","background_6.png","background_7.png",
       "background_8.png","background_9.png"]

pokemons = [Pokemon("Charmander", "Fuego",150,[Ataque("Scratch",30),Ataque("Growl",40),Ataque("Ember",25),Ataque("Smokescreen",20)], Path("Images","Sprites","4_charmander_front.png"), Path("Images","Sprites","4_charmander_back.png")),
             Pokemon("Squirtle", "Agua",150,[Ataque("Headbutt",45),Ataque("Tackle",40),Ataque("Strength",20),Ataque("Skull Bash",10)], Path("Images","Sprites","7_squirtle_front.png"), Path("Images","Sprites","7_squirtle_back.png")),
             Pokemon("Bulbasaur", "Planta",180,[Ataque("Cut",30),Ataque("Bind",15),Ataque("Headbutt",40),Ataque("Tackle",35)], Path("Images","Sprites","1_bulbasaur_front.png"), Path("Images","Sprites","1_bulbasaur_back.png"))]


pygame.init()


#Sound Effects
pygame.mixer.init()
pygame.mixer.music.load(Path("Sound", "pokemon-theme-song-original2.mp3"))
pygame.mixer.music.play()

effectPlink = pygame.mixer.Sound(Path("Sound","plink.mp3"))

clock = pygame.time.Clock()
fuente = Path("Fonts","pokemon_generation_1.ttf")
salir = False
pantalla1 = True
pantalla2 = False
pantalla3 = False
pantalla4 = False

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
            
        if pantalla1:
            #pantalla3 = False
            
            loop = 1
            
            
            # Crear la ventana y poner el tamaño.
            screen = pygame.display.set_mode((400, 630))
            bg = pygame.image.load(Path("Images","bg1.png"))
            # Poner el título de la ventana.

            #Background
            pygame.display.set_caption("Pykemon")
            screen.blit(bg, (0, 0))
            #Texto de escoje tu pokemon
            font = pygame.font.Font(fuente, 11)
            text = font.render('Pulsa para emepzar...', True,(250,250,250))
            screen.blit(text,(230,580))
            #Icon of the game
            programIcon = pygame.image.load(Path("Images","icon.png"))
            pygame.display.set_icon(programIcon)
            

            textBattle1 = "Empieza la batalla!"
            textBattle2, textBattle3 = "",""
            if event.type == pygame.QUIT:
                salir = True
                pantalla1 = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    salir = True
                    pantalla1 = False
                else:
                    pantalla1 = False
                    pantalla2 = True
        #Ventana de escojer pokemon  
        if pantalla2: 
            
            
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
            font = pygame.font.Font(fuente, 18)
            text = font.render('Escoje tu Pokemon ...', True,(0,0,0))
            screen.blit(text,(65,180))   
            
            #Botones para los pokemons
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if pygame.Rect(60, 320, 100, 100).collidepoint(x, y) or pygame.Rect(250, 320, 100, 100).collidepoint(x, y) or pygame.Rect(147, 460, 100, 100).collidepoint(x, y):
                        
                        effectPlink.play()
                        pygame.mixer.music.load(Path("Sound","pokemon-battle.mp3"))
                        pygame.mixer.music.play()
                        pantalla2 = False
                        batalla = True
                        pantalla3 = True
                        pokemonBot = random.choice(pokemons)
                        bgEscenario = random.choice(bgs)
                        if pygame.Rect(60, 320, 100, 100).collidepoint(x, y):
                            pokemonUser = pokemons[0]
                            
                        elif pygame.Rect(250, 320, 100, 100).collidepoint(x, y):
                            pokemonUser = pokemons[1]
                            
                        elif pygame.Rect(147, 460, 100, 100).collidepoint(x, y):
                            pokemonUser = pokemons[2]
                            
                        cb = Combate(pokemonUser, pokemonBot)#Inicializamos el objeto batalla
                        
                        
                            
        if pantalla3:   
            
            
            #PANEL DE BATALLA
            screen.fill([235,240,186])
            
            #Escenario
            escenario = pygame.image.load(Path("Images","Backgrounds",bgEscenario)).convert_alpha()
            screen.blit(pygame.transform.scale(escenario, (350, 250)), (25, 20))
            pygame.draw.rect(screen, (0,0,0), (25,20,350,250),  2, 3)#Borde
            #pokemons
            pokemon1 = pygame.image.load(pokemonUser.getImgBack()).convert_alpha()
            screen.blit(pygame.transform.scale(pokemon1, (100, 100)), (30, 160))
            
            pokemon2 = pygame.image.load(pokemonBot.getImgFront()).convert_alpha()
            screen.blit(pygame.transform.scale(pokemon2, (100, 100)), (230, 70))
            
            #Nombre con hp
            font = pygame.font.Font(fuente, 12)
            nameHp1 = pokemonBot.getName().upper()+": "+str(pokemonBot.getHp())
            text1 = font.render(nameHp1, True,(0,0,0))
            
            screen.blit(text1,(40,40))
            
            nameHp2 = pokemonUser.getName().upper()+": "+str(pokemonUser.getHp())
            text2 = font.render(nameHp2, True,(0,0,0))
            
            screen.blit(text2,(210,230)) 
        
            #TextArea del terminal
            pygame.draw.rect(screen, (0,0,0), (25,280,350,110),  2, 3)
            font = pygame.font.Font(fuente, 12)
            
            text1 = font.render(textBattle1, True,(0,0,0))
            screen.blit(text1,(30,290))
            text2 = font.render(textBattle2, True,(0,0,0))
            screen.blit(text2,(30,305))
            text3 = font.render(textBattle3, True,(0,0,0))
            screen.blit(text3,(30,320))
            
            #--Botones de ataques (Esto hay que optimizarlo bastante)
            #for i in range(4):
            pygame.draw.rect(screen, (0,0,0), (25,395,170,100),  2, 3)
            pygame.draw.rect(screen, (0,0,0), (205,395,170,100),  2, 3)
            pygame.draw.rect(screen, (0,0,0), (25,500,170,100),  2, 3)
            pygame.draw.rect(screen, (0,0,0), (205,500,170,100),  2, 3)
            
            #Texto de los ataques
            
            font = pygame.font.Font(fuente, 13)
            ataques = pokemonUser.getAtaques()
            text1 = font.render(ataques[0].getName(), True,(0,0,0))
            screen.blit(text1,(50,410)) 
            
            text2 = font.render(ataques[1].getName(), True,(0,0,0))
            
            screen.blit(text2,(230,410)) 
            
            text3 = font.render(ataques[2].getName(), True,(0,0,0))
            screen.blit(text3,(50,510))
            
            text4 = font.render(ataques[3].getName(), True,(0,0,0))
            
            screen.blit(text4,(230,510))
            if loop == 2 :
                loop += 1
                
            elif loop == 3:
                pantalla3 = False
                option = messagebox.askyesno(message="¿Quieres jugar de nuevo?", title="GAME OVER")
                
                if option:
                    pantalla1 = True
                    pygame.mixer.music.load(Path("Sound","pokemon-theme-song-original2.mp3"))
                    pygame.mixer.music.play()
                else:
                    salir = True
            #Botones de los ataques
            if batalla:#Esta condicion es para que no se puedan pulsar los botones si uno de los pokemons ha muerto
                x, y = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        if pygame.Rect(25, 395, 170, 100).collidepoint(x, y) or pygame.Rect(205,395,170,100).collidepoint(x, y) or pygame.Rect(25,500,170,100).collidepoint(x, y) or pygame.Rect(205,500,170,100).collidepoint(x, y):
                            effectPlink.play()
                            #Ataque del usuario
                            if pygame.Rect(25,395, 170,100).collidepoint(x, y):
                                ataqueUser = ataques[0]
                            elif pygame.Rect(205,395,170,100).collidepoint(x, y):
                                ataqueUser = ataques[1]
                            elif pygame.Rect(25,500,170,100).collidepoint(x, y):
                                ataqueUser = ataques[2]
                            elif pygame.Rect(205,500,170,100).collidepoint(x, y):
                                ataqueUser = ataques[3]
                            #Ataque del bot
                            ataqueBot = random.choice(pokemonBot.getAtaques())
                            
                            #Daño del usuario
                            textTerminal = cb.ronda(ataqueUser,ataqueBot)
                            textBattle1 = textTerminal[0]
                            textBattle2 = textTerminal[1]
                            textBattle3 = textTerminal[2]
                            
                            #Comprobar si uno de los dos a muertos
                            if pokemonUser.getHp() <= 0 or pokemonBot.getHp() <= 0:
                                batalla = False
                                pygame.mixer.music.load(Path("Sound","win.mp3"))
                                pygame.mixer.music.play()
                                loop +=1
                                
                                if pokemonUser.getHp() <= 0:
                                    ganador = pokemonBot.getName()
                                else:
                                    ganador = pokemonUser.getName()
                                
        
            
            
            
                
    # Actualizar la pantalla.
    pygame.display.flip()
    pygame.display.update()

# Cerrar Pygame y liberar los recursos que pidió el programa.
pygame.quit()
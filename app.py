"""
TAREAS:
- Hacer bonita la terminal de pokemon
- Crear un bucle para continuar jugando aunque se acabe la partida, agrupando desde el init() y si es necesario con recursividad
- Crear ventana final que muestre quien ha ganado, foto del pokemo y si quiere volver a jugar o salir del programa
- Arreglar problema de las dependencias de la env del proyecto
"""


# Importar e inicializar Pygame
import pygame
import random
from pokemons import *
from tkinter import messagebox as MessageBox
def combate(pokemonUser, pokemonBot, ataqueuUser, ataqueBot):
    #Ataque del usuario
    pokemonBot.setHp(pokemonBot.getHp()-ataqueuUser.getDamage())
    #Ataque del bot
    pokemonUser.setHp(pokemonUser.getHp()-ataqueBot.getDamage())

    texto = pokemonUser.getName() + " uso " + ataqueUser.getName()
    texto += ", " + pokemonBot.getName() + " uso " + ataqueBot.getName() + "."
    
    #texto += "Tu pokemon tiene " + str(pokemonUser.getHp()) + " de vida" + ", el pokemon del bot tiene " + str(pokemonBot.getHp()) + " de vida"

    #Si el pokemon del usuario muere
    if pokemonUser.getHp() <= 0:
        pokemonUser.setHp(0)
        texto += " Tu pokemon ha muerto"
        #MessageBox.showinfo("GAME OVER", "Tu pokemon ha muerto")
    #Si el pokemon del bot muere
    if pokemonBot.getHp() <= 0:
        pokemonBot.setHp(0)
        texto += " El pokemon del bot ha muerto"
        #MessageBox.showinfo("CONGRATULATIONS", "Tu pokemon ha ganado")
        
    
    return texto


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
pantalla4 = False

textBattle = "Empieza la batalla!"
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
            font = pygame.font.Font('Fonts/pokemon_generation_1.ttf', 18)
            text = font.render('Escoje tu Pokemon ...', True,(0,0,0))
            screen.blit(text,(65,180))   
            
            #Botones para los pokemons
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if pygame.Rect(60, 320, 100, 100).collidepoint(x, y) or pygame.Rect(250, 320, 100, 100).collidepoint(x, y) or pygame.Rect(147, 460, 100, 100).collidepoint(x, y):
                        pantalla2 = False
                        pantalla3 = True
                        pokemonBot = random.choice(pokemons)
                        bgEscenario = random.choice(bgs)
                        batalla = True
                        if pygame.Rect(60, 320, 100, 100).collidepoint(x, y):
                            pokemonUser = pokemons[0]
                            
                        elif pygame.Rect(250, 320, 100, 100).collidepoint(x, y):
                            pokemonUser = pokemons[1]
                            
                        elif pygame.Rect(147, 460, 100, 100).collidepoint(x, y):
                            pokemonUser = pokemons[2]
                            
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
            
            screen.blit(text1,(40,40))
            
            nameHp2 = pokemonUser.getName().upper()+": "+str(pokemonUser.getHp())
            text2 = font.render(nameHp2, True,(0,0,0))
            
            screen.blit(text2,(210,230)) 
        
            #TextArea del terminal
            pygame.draw.rect(screen, (0,0,0), (25,280,350,110),  2, 3)
            font = pygame.font.Font('Fonts/pokemon_generation_1.ttf', 9)
            
            text1 = font.render(textBattle, True,(0,0,0))
            screen.blit(text1,(30,290))
            
            #--Botones de ataques (Esto hay que optimizarlo bastante)
            #for i in range(4):
            pygame.draw.rect(screen, (0,0,0), (25,395,170,100),  2, 3)
            pygame.draw.rect(screen, (0,0,0), (205,395,170,100),  2, 3)
            pygame.draw.rect(screen, (0,0,0), (25,500,170,100),  2, 3)
            pygame.draw.rect(screen, (0,0,0), (205,500,170,100),  2, 3)
            
            #Texto de los ataques
            
            font = pygame.font.Font('Fonts/pokemon_generation_1.ttf', 13)
            ataques = pokemonUser.getAtaques()
            text1 = font.render(ataques[0].getName(), True,(0,0,0))
            screen.blit(text1,(50,410)) 
            
            text2 = font.render(ataques[1].getName(), True,(0,0,0))
            
            screen.blit(text2,(230,410)) 
            
            text3 = font.render(ataques[2].getName(), True,(0,0,0))
            screen.blit(text3,(50,510))
            
            text4 = font.render(ataques[3].getName(), True,(0,0,0))
            
            screen.blit(text4,(230,510))
        
            #Botones de los ataques
            if batalla:#Esta condicion es para que no se puedan pulsar los botones si uno de los pokemons ha muerto
                x, y = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        if pygame.Rect(25, 395, 170, 100).collidepoint(x, y) or pygame.Rect(205,395,170,100).collidepoint(x, y) or pygame.Rect(25,500,170,100).collidepoint(x, y) or pygame.Rect(205,500,170,100).collidepoint(x, y):
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
                            
                            #Preferiria que me devolviese una lista con varios textos y elementos
                            textBattle = combate(pokemonUser, pokemonBot, ataqueUser, ataqueBot)
                            
                            if pokemonUser.getHp() <= 0 or pokemonBot.getHp() <= 0:
                                batalla = False
                                #pantalla3 = False
                                pantalla4 = True
                                if pokemonUser.getHp() <= 0:
                                    ganador = pokemonBot.getName()
                                else:
                                    ganador = pokemonUser.getName()
        if pantalla4:
            #PANEL DE BATALLA
            screen.fill([235,240,186])
            
                
    # Actualizar la pantalla.
    pygame.display.flip()
    pygame.display.update()

# Cerrar Pygame y liberar los recursos que pidió el programa.
pygame.quit()


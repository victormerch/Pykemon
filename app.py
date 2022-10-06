# Importar e inicializar Pygame.
import pygame
pygame.init()

# Crear la ventana y poner el tamaño.
screen = pygame.display.set_mode((400, 630))
bg = pygame.image.load("Images/bg1.png")
# Poner el título de la ventana.

#Background
pygame.display.set_caption("Pykemon")
screen.blit(bg, (0, 0))
#Icon of the game
programIcon = pygame.image.load('Images/icon.png')
pygame.display.set_icon(programIcon)

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
 

clock = pygame.time.Clock()
salir = False

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
                #Cambiamos el color de fondo
                screen.fill([235, 240, 186])
                #Añadimos los pokemons
                pokemon1 = pygame.image.load("Images/Sprites/4_charmander_front.png").convert_alpha()
                pokemon2 = pygame.image.load("Images/Sprites/7_squirtle_front.png").convert_alpha()
                pokemon3 = pygame.image.load("Images/Sprites/1_bulbasaur_front.png").convert_alpha()
                screen.blit(pygame.transform.scale(pokemon1, (100, 100)), (60, 320))
                screen.blit(pygame.transform.scale(pokemon2, (100, 100)), (250, 320))
                screen.blit(pygame.transform.scale(pokemon3, (100, 100)), (147, 460))
                
                
    # Actualizar la pantalla.
    pygame.display.flip()
    pygame.display.update()

# Cerrar Pygame y liberar los recursos que pidió el programa.
pygame.quit()

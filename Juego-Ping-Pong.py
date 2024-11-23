"""Module providingFunction printing python version"""
import sys
import random
import pygame

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
screen = pygame.display.set_mode((1300,700))
Anchura_Pantalla = 1300
Altura_Pantalla = 700
pygame.display.set_caption("Pin Ponk")

# Configurar el título de la pantalla
pygame.display.set_caption("Menú del juego")

# Configurar el reloj
clock = pygame.time.Clock()

# Configurar los colores
white = (255, 255, 255)
negro = (0, 0, 0)
black = (0, 0, 0)
red = (255, 0, 0)
verde = (0, 255, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)

# Configurar la fuente
font = pygame.font.Font(None, 50)
# Configurar la fuente
fontt = pygame.font.Font(None, 100)
# Función para mostrar texto en la pantalla

# Velocidad pelota
ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = 3 * random.choice((1, -1))
ball_speed_x_medio = 6 * random.choice((1, -1))
ball_speed_y_medio = 4 * random.choice((1, -1))
ball_speed_x_dificil = 7 * random.choice((1, -1))
ball_speed_y_dificil = 5 * random.choice((1, -1))
jugador_speed = 0
oponente_speed = 15


def display_text(text, x, y):
    text = font.render(text, True, rojo)
    text_rect = text.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    screen.blit(text, text_rect)

# Función para mostrar texto en la pantalla


def display_text2(text, x, y):
    text = fontt.render(text, True, azul)
    text_rect = text.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    screen.blit(text, text_rect)


def dispaly_text_multiline(text, x, y):
    lines = text.splitlines()

    for i, line in enumerate(lines):
        line_surface = font.render(line, True, rojo)
        line_rect = line_surface.get_rect()
        line_rect.centerx = x
        line_rect.centery = y+i * font.get_linesize()*2
        screen.blit(line_surface, line_rect)

# Funcion movimiento pelota


def movimiento_pelota():

    global ball_speed_x, ball_speed_y, jugador_contador, oponente_contador, score_time

    pelota.x += ball_speed_x
    pelota.y += ball_speed_y

    if pelota.top <= 0 or pelota.bottom >= Altura_Pantalla:
        ball_speed_y *= -1

    if pelota.left <= 0:
        jugador_contador += 1
        score_time = pygame.time.get_ticks()

    if pelota.right >= Anchura_Pantalla:
        oponente_contador += 1
        score_time = pygame.time.get_ticks()

    if pelota.colliderect(jugador) or pelota.colliderect(oponente):
        ball_speed_x *= -1


def movimiento_pelota_normal():

    global ball_speed_x_medio, ball_speed_y_medio, jugador_contador, oponente_contador, score_time

    pelota.x += ball_speed_x_medio
    pelota.y += ball_speed_y_medio

    if pelota.top <= 0 or pelota.bottom >= Altura_Pantalla:
        ball_speed_y_medio *= -1

    if pelota.left <= 0:
        jugador_contador += 1
        score_time = pygame.time.get_ticks()

    if pelota.right >= Anchura_Pantalla:
        oponente_contador += 1
        score_time = pygame.time.get_ticks()

    if pelota.colliderect(jugador) or pelota.colliderect(oponente):
        ball_speed_x_medio *= -1


def movimiento_pelota_dificil():

    global ball_speed_x_dificil, ball_speed_y_dificil, jugador_contador, oponente_contador, score_time

    pelota.x += ball_speed_x_dificil
    pelota.y += ball_speed_y_dificil

    if pelota.top <= 0 or pelota.bottom >= Altura_Pantalla:
        ball_speed_y_dificil *= -1

    if pelota.left <= 0:
        jugador_contador += 1
        score_time = pygame.time.get_ticks()

    if pelota.right >= Anchura_Pantalla:
        oponente_contador += 1
        score_time = pygame.time.get_ticks()

    if pelota.colliderect(jugador) or pelota.colliderect(oponente):
        ball_speed_x_dificil *= -1

# Mas funciones


def movimiento_jugador():
    jugador.y += jugador_speed
    if jugador.top <= 0:
        jugador.top = 0
    if jugador.bottom >= Altura_Pantalla:
        jugador.bottom = Altura_Pantalla


def ai_oponente():

    if oponente.top < pelota.y:
        oponente.y += oponente_speed
    if oponente.bottom > pelota.y:
        oponente.y -= oponente_speed
    if jugador.top <= 0:
        jugador.top = 0
    if jugador.bottom >= Altura_Pantalla:
        jugador.bottom = Altura_Pantalla


def input_jugador(event):

    global jugador_speed

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_DOWN:
            jugador_speed += 3
        if event.key == pygame.K_UP:
            jugador_speed -= 3

    if event.type == pygame.KEYUP:

        if event.key == pygame.K_DOWN:
            jugador_speed -= 3
        if event.key == pygame.K_UP:
            jugador_speed += 3


def input_jugador2(event):

    global jugador_speed

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_DOWN:
            jugador_speed += 5
        if event.key == pygame.K_UP:
            jugador_speed -= 5

    if event.type == pygame.KEYUP:

        if event.key == pygame.K_DOWN:
            jugador_speed -= 5
        if event.key == pygame.K_UP:
            jugador_speed += 5


def reaparece():
    global ball_speed_y, ball_speed_x, score_time

    current_time = pygame.time.get_ticks()
    pelota.center = (Anchura_Pantalla/2, Altura_Pantalla/2)

    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0, 0
    else:
        ball_speed_y = 2 * random.choice((1, -1))
        ball_speed_x = 3 * random.choice((1, -1))
        score_time = None


def reaparece_normal():
    global ball_speed_y_medio, ball_speed_x_medio, score_time

    current_time = pygame.time.get_ticks()
    pelota.center = (Anchura_Pantalla/2, Altura_Pantalla/2)

    if current_time - score_time < 2100:
        ball_speed_x_medio, ball_speed_y_medio = 0, 0
    else:
        ball_speed_y_medio = 3 * random.choice((1, -1))
        ball_speed_x_medio = 4 * random.choice((1, -1))
        score_time = None


def reaparece_dificil():
    global ball_speed_y, ball_speed_x, score_time

    current_time = pygame.time.get_ticks()
    pelota.center = (Anchura_Pantalla/2, Altura_Pantalla/2)

    if current_time - score_time < 2100:
        ball_speed_x_dificil, ball_speed_y_dificil = 0, 0
    else:
        ball_speed_y_dificil = 6 * random.choice((1, -1))
        ball_speed_x_dificil = 4 * random.choice((1, -1))
        score_time = None


# Dibujar formas geometricas
pelota = pygame.Rect(Anchura_Pantalla/2 - 15, Altura_Pantalla/2 - 15, 30, 30)
jugador = pygame.Rect(Anchura_Pantalla - 20, Altura_Pantalla/2 - 70, 10, 140)
oponente = pygame.Rect(10, Altura_Pantalla/2 - 70, 10, 140)
circulo = pygame.Rect(Anchura_Pantalla/2 - 75,
                      Altura_Pantalla/2 - 75, 150, 150)
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

# Variables texto
jugador_contador = 0
oponente_contador = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)

# Variables del contador
score_time = None

# Función para el menú del juego


def game_menu():
    
    global ball_speed_y, ball_speed_x,jugador_contador,oponente_contador
    
    menu_items = ["Iniciar juego", "Ver créditos", "Cerrar juego"]
    selected_index = 0
    exit_menu = False
    exit_menu_principal = False
    
    while not exit_menu_principal:
        # Manejar eventos
        menu_items = ["Iniciar juego", "Ver créditos", "Cerrar juego"]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_index = (selected_index - 1) % len(menu_items)
                elif event.key == pygame.K_DOWN:
                    selected_index = (selected_index + 1) % len(menu_items)
                elif event.key == pygame.K_RETURN:
                    
                    #Escoje Iniciar Juego --> Menu de dificultad
                    if selected_index == 0:
                        
                        menu_items = ["Facil", "Normal", "Dificil", "Atras"]
                        selected_index = 0
                        exit_menu = False
                        

                        # Menu de dificultad
                        while not exit_menu:
                            # Manejar eventos
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    sys.exit()
                                elif event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_UP:
                                        selected_index = (selected_index - 1) % len(menu_items)
                                    elif event.key == pygame.K_DOWN:
                                        selected_index = (selected_index + 1) % len(menu_items)
                                    elif event.key == pygame.K_RETURN:
                                        print(f"selected index:{selected_index}")

                                        # Seleciona facil --> Menu de puntos
                                        if selected_index == 0:
                                            menu_items = ["5 Puntos", "10 Puntos", "20 Puntos","Atras"]
                                            selected_index = 0
                                            exit_menu = False
                                            
                                            # Menu de puntos facil
                                            while not exit_menu:
                                                # Manejar eventos
                                                for event in pygame.event.get():
                                                    if event.type == pygame.QUIT:
                                                        sys.exit()
                                                    elif event.type == pygame.KEYDOWN:
                                                        if event.key == pygame.K_UP:
                                                            selected_index = (selected_index - 1) % len(menu_items)
                                                        elif event.key == pygame.K_DOWN:
                                                            selected_index = (selected_index + 1) % len(menu_items)
                                                        elif event.key == pygame.K_RETURN:
                                                            
                                                            print(f"selected index:{selected_index}")
                                                            
                                                            #Juego en facil que termine con 5 puntos
                                                            if selected_index == 0:
                                                                
                                                                exit_menu_juego = False
                                                                while not exit_menu_juego:
                                                                    for event in pygame.event.get():
                                                                        if event.type == pygame.QUIT:
                                                                            pygame.quit()
                                                                            sys.exit()

                                                                        # movimiento jugador (input)
                                                                        input_jugador(event)

                                                                    # Movimientos
                                                                    movimiento_pelota()
                                                                    movimiento_jugador()
                                                                    ai_oponente()

                                                                    # VisualesP
                                                                    # Color de la pantalla
                                                                    screen.fill(negro)
                                                                    pygame.draw.rect(
                                                                        screen, light_grey, jugador)
                                                                    pygame.draw.rect(
                                                                        screen, light_grey, oponente)
                                                                    pygame.draw.ellipse(
                                                                        screen, rojo, pelota,)
                                                                    pygame.draw.aaline(
                                                                        screen, light_grey, (Anchura_Pantalla/2, 0), (Anchura_Pantalla/2, Altura_Pantalla))
                                                                    pygame.draw.ellipse(
                                                                        screen, light_grey, circulo, 1)
                                                                    
                                                                    #Reaparece la pelota
                                                                    if score_time:
                                                                        reaparece()
                                                                    
                                                                    # Funciones de texto
                                                                    player_text = game_font.render(
                                                                        f"{jugador_contador}", False, light_grey)
                                                                    screen.blit(
                                                                        player_text, (700, 480))

                                                                    oponente_text = game_font.render(
                                                                        f"{oponente_contador}", False, light_grey)
                                                                    screen.blit(
                                                                        oponente_text, (645, 480))
                                                                    
                                                                    #Cuando llegue a 5 puntos para
                                                                    
                                                                    #El juego se para i se muestra quien gano i quien perdio.
                                                                    #Tambien se muestra la opcion de volver al menu inicial.
                                                                    if jugador_contador >= 5:
                                                                        player_text_win = game_font.render(
                                                                            "Loser:(", False, light_grey )
                                                                        screen.blit(player_text_win,(340,300))
                                                                        
                                                                        oponente_text_lost = game_font.render(
                                                                            "Winer!", False, light_grey)
                                                                        screen.blit(oponente_text_lost, (1002,300))

                                                                        ball_speed_x = 0
                                                                        ball_speed_y = 0

                                                                        menu_items = ["Volver menu inicial"]
                                                                        selected_index = 0
                                                                        exit_menu = False
                                                                        
                                                                        # Opcion volver menu inicial
                                                                        while not exit_menu:
                                                                            # Manejar eventos
                                                                            for event in pygame.event.get():
                                                                                if event.type == pygame.QUIT:
                                                                                    sys.exit()
                                                                                elif event.type == pygame.KEYDOWN:
                                                                                    if event.key == pygame.K_UP:
                                                                                        selected_index = (selected_index - 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_DOWN:
                                                                                        selected_index = (selected_index + 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_RETURN:
                                                                                        if selected_index == 0:
                                                                                            exit_menu = True
                                                                                            exit_menu_juego = True
                                                                            
                                                                            

                                                                            # Mostrar opciones del menú
                                                                            
                                                                            for index, item in enumerate(menu_items):
                                                                                if index == selected_index:
                                                                                    display_text(
                                                                                        "> " + item, 1020, 500 + index * 100)
                                                                                else:
                                                                                    display_text(
                                                                                        item, 1020, 500 + index * 100)

                                                                            # Actualizar la pantalla
                                                                            pygame.display.update()

                                                                            # Controlar la velocidad de actualización de la pantalla
                                                                            clock.tick(60)
                                                                    
                                                                    #El juego se para i se muestra quien gano i quien perdio.
                                                                    #Tambien se muestra la opcion de volver al menu inicial.
                                                                    elif oponente_contador >= 5:
                                                                        player_text_win = game_font.render(
                                                                            "Winer!", False, light_grey )
                                                                        screen.blit(player_text_win,(340,300))
                                                                        
                                                                        oponente_text_lost = game_font.render(
                                                                            "Loser:(", False, light_grey)
                                                                        screen.blit(oponente_text_lost, (1002,300))

                                                                        ball_speed_x = 0
                                                                        ball_speed_y = 0

                                                                        menu_items = ["Volver menu inicial"]
                                                                        selected_index = 0
                                                                        exit_menu = False
                                                                        
                                                                        # Menu de puntos facil
                                                                        while not exit_menu:
                                                                            # Manejar eventos
                                                                            for event in pygame.event.get():
                                                                                if event.type == pygame.QUIT:
                                                                                    sys.exit()
                                                                                elif event.type == pygame.KEYDOWN:
                                                                                    if event.key == pygame.K_UP:
                                                                                        selected_index = (selected_index - 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_DOWN:
                                                                                        selected_index = (selected_index + 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_RETURN:
                                                                                        if selected_index == 0:
                                                                                            exit_menu = True
                                                                                            exit_menu_juego = True
                                                                            
                                                                            

                                                                            # Mostrar opciones del menú
                                                                            
                                                                            for index, item in enumerate(menu_items):
                                                                                if index == selected_index:
                                                                                    display_text(
                                                                                        "> " + item, 1020, 500 + index * 100)
                                                                                else:
                                                                                    display_text(
                                                                                        item, 1020, 500 + index * 100)

                                                                            # Actualizar la pantalla
                                                                            pygame.display.update()

                                                                            # Controlar la velocidad de actualización de la pantalla
                                                                            clock.tick(60)

                                                                    # Recargar la ventana
                                                                    pygame.display.flip()
                                                                    clock.tick(200)


                                                                pass
                                                            
                                                            #Juego en facil que termine con 10 puntos
                                                            elif selected_index == 1:
                                                                
                                                                exit_menu_juego = False
                                                                while not exit_menu_juego:
                                                                    for event in pygame.event.get():
                                                                        if event.type == pygame.QUIT:
                                                                            pygame.quit()
                                                                            sys.exit()

                                                                        # movimiento jugador (input)
                                                                        input_jugador(event)

                                                                    # Movimientos
                                                                    movimiento_pelota()
                                                                    movimiento_jugador()
                                                                    ai_oponente()

                                                                    # VisualesP
                                                                    # Color de la pantalla
                                                                    screen.fill(negro)
                                                                    pygame.draw.rect(
                                                                        screen, light_grey, jugador)
                                                                    pygame.draw.rect(
                                                                        screen, light_grey, oponente)
                                                                    pygame.draw.ellipse(
                                                                        screen, rojo, pelota,)
                                                                    pygame.draw.aaline(
                                                                        screen, light_grey, (Anchura_Pantalla/2, 0), (Anchura_Pantalla/2, Altura_Pantalla))
                                                                    pygame.draw.ellipse(
                                                                        screen, light_grey, circulo, 1)
                                                                    if score_time:
                                                                        reaparece()
                                                                    player_text = game_font.render(
                                                                        f"{jugador_contador}", False, light_grey)
                                                                    screen.blit(
                                                                        player_text, (700, 480))

                                                                    oponente_text = game_font.render(
                                                                        f"{oponente_contador}", False, light_grey)
                                                                    screen.blit(
                                                                        oponente_text, (645, 480))

                                                                    #El juego se para i se muestra quien gano i quien perdio.
                                                                    #Tambien se muestra la opcion de volver al menu inicial.
                                                                    if jugador_contador >= 10:
                                                                        player_text_win = game_font.render(
                                                                            "Loser:(", False, light_grey )
                                                                        screen.blit(player_text_win,(340,300))
                                                                        
                                                                        oponente_text_lost = game_font.render(
                                                                            "Winer!", False, light_grey)
                                                                        screen.blit(oponente_text_lost, (1002,300))

                                                                        ball_speed_x = 0
                                                                        ball_speed_y = 0

                                                                        menu_items = ["Volver menu inicial"]
                                                                        selected_index = 0
                                                                        exit_menu = False
                                                                        
                                                                        # Menu de puntos facil
                                                                        while not exit_menu:
                                                                            # Manejar eventos
                                                                            for event in pygame.event.get():
                                                                                if event.type == pygame.QUIT:
                                                                                    sys.exit()
                                                                                elif event.type == pygame.KEYDOWN:
                                                                                    if event.key == pygame.K_UP:
                                                                                        selected_index = (selected_index - 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_DOWN:
                                                                                        selected_index = (selected_index + 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_RETURN:
                                                                                        if selected_index == 0:
                                                                                            exit_menu = True
                                                                                            exit_menu_juego = True
                                                                            
                                                                            

                                                                            # Mostrar opciones del menú
                                                                            
                                                                            for index, item in enumerate(menu_items):
                                                                                if index == selected_index:
                                                                                    display_text(
                                                                                        "> " + item, 1020, 500 + index * 100)
                                                                                else:
                                                                                    display_text(
                                                                                        item, 1020, 500 + index * 100)

                                                                            # Actualizar la pantalla
                                                                            pygame.display.update()

                                                                            # Controlar la velocidad de actualización de la pantalla
                                                                            clock.tick(60)
                                                                    
                                                                    #El juego se para i se muestra quien gano i quien perdio.
                                                                    #Tambien se muestra la opcion de volver al menu inicial.
                                                                    elif oponente_contador >= 10:
                                                                        player_text_win = game_font.render(
                                                                            "Winer!", False, light_grey )
                                                                        screen.blit(player_text_win,(340,300))
                                                                        
                                                                        oponente_text_lost = game_font.render(
                                                                            "Loser:(", False, light_grey)
                                                                        screen.blit(oponente_text_lost, (1002,300))

                                                                        ball_speed_x = 0
                                                                        ball_speed_y = 0

                                                                        menu_items = ["Volver menu inicial"]
                                                                        selected_index = 0
                                                                        exit_menu = False
                                                                        
                                                                        # Menu de puntos facil
                                                                        while not exit_menu:
                                                                            # Manejar eventos
                                                                            for event in pygame.event.get():
                                                                                if event.type == pygame.QUIT:
                                                                                    sys.exit()
                                                                                elif event.type == pygame.KEYDOWN:
                                                                                    if event.key == pygame.K_UP:
                                                                                        selected_index = (selected_index - 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_DOWN:
                                                                                        selected_index = (selected_index + 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_RETURN:
                                                                                        if selected_index == 0:
                                                                                            exit_menu = True
                                                                                            exit_menu_juego = True
                                                                            
                                                                            

                                                                            # Mostrar opciones del menú
                                                                            
                                                                            for index, item in enumerate(menu_items):
                                                                                if index == selected_index:
                                                                                    display_text(
                                                                                        "> " + item, 1020, 500 + index * 100)
                                                                                else:
                                                                                    display_text(
                                                                                        item, 1020, 500 + index * 100)

                                                                            # Actualizar la pantalla
                                                                            pygame.display.update()

                                                                            # Controlar la velocidad de actualización de la pantalla
                                                                            clock.tick(60)

                                                                    # Recargar la ventana
                                                                    pygame.display.flip()
                                                                    clock.tick(200)

                                                                pass 

                                                            #juego en facil que termine con 20 puntos     
                                                            elif selected_index ==2:
                                                                
                                                                exit_menu_juego = False
                                                                while not exit_menu_juego:
                                                                    for event in pygame.event.get():
                                                                        if event.type == pygame.QUIT:
                                                                            pygame.quit()
                                                                            sys.exit()

                                                                        # movimiento jugador (input)
                                                                        input_jugador(event)

                                                                    # Movimientos
                                                                    movimiento_pelota()
                                                                    movimiento_jugador()
                                                                    ai_oponente()

                                                                    # VisualesP
                                                                    # Color de la pantalla
                                                                    screen.fill(negro)
                                                                    pygame.draw.rect(
                                                                        screen, light_grey, jugador)
                                                                    pygame.draw.rect(
                                                                        screen, light_grey, oponente)
                                                                    pygame.draw.ellipse(
                                                                        screen, rojo, pelota,)
                                                                    pygame.draw.aaline(
                                                                        screen, light_grey, (Anchura_Pantalla/2, 0), (Anchura_Pantalla/2, Altura_Pantalla))
                                                                    pygame.draw.ellipse(
                                                                        screen, light_grey, circulo, 1)
                                                                    if score_time:
                                                                        reaparece()
                                                                    player_text = game_font.render(
                                                                        f"{jugador_contador}", False, light_grey)
                                                                    screen.blit(
                                                                        player_text, (700, 480))

                                                                    oponente_text = game_font.render(
                                                                        f"{oponente_contador}", False, light_grey)
                                                                    screen.blit(
                                                                        oponente_text, (645, 480))

                                                                    #El juego se para i se muestra quien gano i quien perdio.
                                                                    #Tambien se muestra la opcion de volver al menu inicial.
                                                                    if jugador_contador >= 20:
                                                                        player_text_win = game_font.render(
                                                                            "Loser:(", False, light_grey )
                                                                        screen.blit(player_text_win,(340,300))
                                                                        
                                                                        oponente_text_lost = game_font.render(
                                                                            "Winer!", False, light_grey)
                                                                        screen.blit(oponente_text_lost, (1002,300))

                                                                        ball_speed_x = 0
                                                                        ball_speed_y = 0

                                                                        menu_items = ["Volver menu inicial"]
                                                                        selected_index = 0
                                                                        exit_menu = False
                                                                        
                                                                        # Menu de puntos facil
                                                                        while not exit_menu:
                                                                            # Manejar eventos
                                                                            for event in pygame.event.get():
                                                                                if event.type == pygame.QUIT:
                                                                                    sys.exit()
                                                                                elif event.type == pygame.KEYDOWN:
                                                                                    if event.key == pygame.K_UP:
                                                                                        selected_index = (selected_index - 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_DOWN:
                                                                                        selected_index = (selected_index + 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_RETURN:
                                                                                        if selected_index == 0:
                                                                                            exit_menu = True
                                                                                            exit_menu_juego = True
                                                                            
                                                                            

                                                                            # Mostrar opciones del menú
                                                                            
                                                                            for index, item in enumerate(menu_items):
                                                                                if index == selected_index:
                                                                                    display_text(
                                                                                        "> " + item, 1020, 500 + index * 100)
                                                                                else:
                                                                                    display_text(
                                                                                        item, 1020, 500 + index * 100)

                                                                            # Actualizar la pantalla
                                                                            pygame.display.update()

                                                                            # Controlar la velocidad de actualización de la pantalla
                                                                            clock.tick(60)
                                                                    
                                                                    #El juego se para i se muestra quien gano i quien perdio.
                                                                    #Tambien se muestra la opcion de volver al menu inicial.
                                                                    elif oponente_contador >= 20:
                                                                        player_text_win = game_font.render(
                                                                            "Winer!", False, light_grey )
                                                                        screen.blit(player_text_win,(340,300))
                                                                        
                                                                        oponente_text_lost = game_font.render(
                                                                            "Loser:(", False, light_grey)
                                                                        screen.blit(oponente_text_lost, (1002,300))

                                                                        ball_speed_x = 0
                                                                        ball_speed_y = 0

                                                                        menu_items = ["Volver menu inicial"]
                                                                        selected_index = 0
                                                                        exit_menu = False
                                                                        
                                                                        # Menu de puntos facil
                                                                        while not exit_menu:
                                                                            # Manejar eventos
                                                                            for event in pygame.event.get():
                                                                                if event.type == pygame.QUIT:
                                                                                    sys.exit()
                                                                                elif event.type == pygame.KEYDOWN:
                                                                                    if event.key == pygame.K_UP:
                                                                                        selected_index = (selected_index - 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_DOWN:
                                                                                        selected_index = (selected_index + 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_RETURN:
                                                                                        if selected_index == 0:
                                                                                            exit_menu = True
                                                                                            exit_menu_juego = True
                                                                            
                                                                            

                                                                            # Mostrar opciones del menú
                                                                            
                                                                            for index, item in enumerate(menu_items):
                                                                                if index == selected_index:
                                                                                    display_text(
                                                                                        "> " + item, 1020, 500 + index * 100)
                                                                                else:
                                                                                    display_text(
                                                                                        item, 1020, 500 + index * 100)

                                                                            # Actualizar la pantalla
                                                                            pygame.display.update()

                                                                            # Controlar la velocidad de actualización de la pantalla
                                                                            clock.tick(60)

                                                                    # Recargar la ventana
                                                                    pygame.display.flip()
                                                                    clock.tick(200)

                                                                pass
                                                                
                                                            #opcion volver al menu principal
                                                            elif selected_index == 3:
                                                                print("opcion'atras'selecionada")
                                                                exit_menu = True
                                                                break
                                                if exit_menu:
                                                    jugador_contador = 0
                                                    oponente_contador = 0
                                                    break       
                                                                

                                                
                                                # Rellenar la pantalla con color negro --> Menu puntos Facil
                                                screen.fill(black)

                                                # Mostrar opciones del menú
                                                display_text2("Puntuacion", 1360/2, 700/2 - 200)
                                                for index, item in enumerate(menu_items):
                                                    if index == selected_index:
                                                        display_text(
                                                            "> " + item, 1360/2, 700/2 + index * 100)
                                                    else:
                                                        display_text(
                                                            item, 1360/2, 700/2 + index * 100)

                                                # Actualizar la pantalla
                                                pygame.display.update()

                                                # Controlar la velocidad de actualización de la pantalla
                                                clock.tick(60)
                                                                
                                        #seleciona el juego en normal --> Menu de puntos                       
                                        elif selected_index == 1:
                                            menu_items = ["5 Puntos", "10 Puntos", "20 Puntos","Atras"]
                                            selected_index = 0
                                            exit_menu = False

                                            while not exit_menu:
                                                # Manejar eventos
                                                for event in pygame.event.get():
                                                    if event.type == pygame.QUIT:
                                                        sys.exit()
                                                    elif event.type == pygame.KEYDOWN:
                                                        if event.key == pygame.K_UP:
                                                            selected_index = (selected_index - 1) % len(menu_items)
                                                        elif event.key == pygame.K_DOWN:
                                                            selected_index = (selected_index + 1) % len(menu_items)
                                                        elif event.key == pygame.K_RETURN:
                                                            
                                                            print(f"selected index:{selected_index}")
                                                            
                                                            #Juego en normal que termine con 5 puntos
                                                            if selected_index == 0:
                                                                
                                                                exit_menu_juego = False

                                                                while not exit_menu_juego:
                                                                    for event in pygame.event.get():
                                                                        if event.type == pygame.QUIT:
                                                                            pygame.quit()
                                                                            sys.exit()

                                                                        # movimiento jugador (input)

                                                                        input_jugador2(event)

                                                                    # Movimientos
                                                                    movimiento_pelota_normal()
                                                                    movimiento_jugador()
                                                                    ai_oponente()

                                                                    # Visuales
                                                                    # Color de la pantalla
                                                                    screen.fill(negro)
                                                                    pygame.draw.rect(
                                                                        screen, light_grey, jugador)
                                                                    pygame.draw.rect(
                                                                        screen, light_grey, oponente)
                                                                    pygame.draw.ellipse(
                                                                        screen, rojo, pelota,)
                                                                    pygame.draw.aaline(
                                                                        screen, light_grey, (Anchura_Pantalla/2, 0), (Anchura_Pantalla/2, Altura_Pantalla))
                                                                    pygame.draw.ellipse(
                                                                        screen, light_grey, circulo, 1)
                                                                    if score_time:
                                                                        reaparece()
                                                                    player_text = game_font.render(
                                                                        f"{jugador_contador}", False, light_grey)
                                                                    screen.blit(
                                                                        player_text, (700, 480))

                                                                    oponente_text = game_font.render(
                                                                        f"{oponente_contador}", False, light_grey)
                                                                    screen.blit(
                                                                        oponente_text, (645, 480))

                                                                    #El juego se para i se muestra quien gano i quien perdio.
                                                                    #Tambien se muestra la opcion de volver al menu inicial.
                                                                    if jugador_contador >= 5:
                                                                        player_text_win = game_font.render(
                                                                            "Loser:(", False, light_grey )
                                                                        screen.blit(player_text_win,(340,300))
                                                                        
                                                                        oponente_text_lost = game_font.render(
                                                                            "Winer!", False, light_grey)
                                                                        screen.blit(oponente_text_lost, (1002,300))

                                                                        ball_speed_x = 0
                                                                        ball_speed_y = 0

                                                                        menu_items = ["Volver menu inicial"]
                                                                        selected_index = 0
                                                                        exit_menu = False
                                                                        
                                                                        # Menu de puntos facil
                                                                        while not exit_menu:
                                                                            # Manejar eventos
                                                                            for event in pygame.event.get():
                                                                                if event.type == pygame.QUIT:
                                                                                    sys.exit()
                                                                                elif event.type == pygame.KEYDOWN:
                                                                                    if event.key == pygame.K_UP:
                                                                                        selected_index = (selected_index - 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_DOWN:
                                                                                        selected_index = (selected_index + 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_RETURN:
                                                                                        if selected_index == 0:
                                                                                            exit_menu = True
                                                                                            exit_menu_juego = True
                                                                            
                                                                            

                                                                            # Mostrar opciones del menú
                                                                            
                                                                            for index, item in enumerate(menu_items):
                                                                                if index == selected_index:
                                                                                    display_text(
                                                                                        "> " + item, 1020, 500 + index * 100)
                                                                                else:
                                                                                    display_text(
                                                                                        item, 1020, 500 + index * 100)

                                                                            # Actualizar la pantalla
                                                                            pygame.display.update()

                                                                            # Controlar la velocidad de actualización de la pantalla
                                                                            clock.tick(60)
                                                                    
                                                                    #El juego se para i se muestra quien gano i quien perdio.
                                                                    #Tambien se muestra la opcion de volver al menu inicial.
                                                                    elif oponente_contador >= 5:
                                                                        player_text_win = game_font.render(
                                                                            "Winer!", False, light_grey )
                                                                        screen.blit(player_text_win,(340,300))
                                                                        
                                                                        oponente_text_lost = game_font.render(
                                                                            "Loser:(", False, light_grey)
                                                                        screen.blit(oponente_text_lost, (1002,300))

                                                                        ball_speed_x = 0
                                                                        ball_speed_y = 0

                                                                        menu_items = ["Volver menu inicial"]
                                                                        selected_index = 0
                                                                        exit_menu = False
                                                                        
                                                                        # Menu de puntos facil
                                                                        while not exit_menu:
                                                                            # Manejar eventos
                                                                            for event in pygame.event.get():
                                                                                if event.type == pygame.QUIT:
                                                                                    sys.exit()
                                                                                elif event.type == pygame.KEYDOWN:
                                                                                    if event.key == pygame.K_UP:
                                                                                        selected_index = (selected_index - 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_DOWN:
                                                                                        selected_index = (selected_index + 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_RETURN:
                                                                                        if selected_index == 0:
                                                                                            exit_menu = True
                                                                                            exit_menu_juego = True
                                                                            
                                                                            

                                                                            # Mostrar opciones del menú
                                                                            
                                                                            for index, item in enumerate(menu_items):
                                                                                if index == selected_index:
                                                                                    display_text(
                                                                                        "> " + item, 1020, 500 + index * 100)
                                                                                else:
                                                                                    display_text(
                                                                                        item, 1020, 500 + index * 100)

                                                                            # Actualizar la pantalla
                                                                            pygame.display.update()

                                                                            # Controlar la velocidad de actualización de la pantalla
                                                                            clock.tick(60)

                                                                    # Recargar la ventana
                                                                    pygame.display.flip()
                                                                    clock.tick(200)

                                                                pass
                                                            
                                                            #Juego en normal que termine con 10 puntos    
                                                            elif selected_index == 1:
                                                                
                                                                exit_menu_juego = False

                                                                while not exit_menu_juego:
                                                                    for event in pygame.event.get():
                                                                        if event.type == pygame.QUIT:
                                                                            pygame.quit()
                                                                            sys.exit()

                                                                        # movimiento jugador (input)

                                                                        input_jugador2(event)

                                                                    # Movimientos
                                                                    movimiento_pelota_normal()
                                                                    movimiento_jugador()
                                                                    ai_oponente()

                                                                    # Visuales
                                                                    # Color de la pantalla
                                                                    screen.fill(negro)
                                                                    pygame.draw.rect(
                                                                        screen, light_grey, jugador)
                                                                    pygame.draw.rect(
                                                                        screen, light_grey, oponente)
                                                                    pygame.draw.ellipse(
                                                                        screen, rojo, pelota,)
                                                                    pygame.draw.aaline(
                                                                        screen, light_grey, (Anchura_Pantalla/2, 0), (Anchura_Pantalla/2, Altura_Pantalla))
                                                                    pygame.draw.ellipse(
                                                                        screen, light_grey, circulo, 1)
                                                                    if score_time:
                                                                        reaparece()
                                                                    player_text = game_font.render(
                                                                        f"{jugador_contador}", False, light_grey)
                                                                    screen.blit(
                                                                        player_text, (700, 480))

                                                                    oponente_text = game_font.render(
                                                                        f"{oponente_contador}", False, light_grey)
                                                                    screen.blit(
                                                                        oponente_text, (645, 480))

                                                                    #El juego se para i se muestra quien gano i quien perdio.
                                                                    #Tambien se muestra la opcion de volver al menu inicial.
                                                                    if jugador_contador >= 10:
                                                                        player_text_win = game_font.render(
                                                                            "Loser:(", False, light_grey )
                                                                        screen.blit(player_text_win,(340,300))
                                                                        
                                                                        oponente_text_lost = game_font.render(
                                                                            "Winer!", False, light_grey)
                                                                        screen.blit(oponente_text_lost, (1002,300))

                                                                        ball_speed_x = 0
                                                                        ball_speed_y = 0

                                                                        menu_items = ["Volver menu inicial"]
                                                                        selected_index = 0
                                                                        exit_menu = False
                                                                        
                                                                        # Menu de puntos facil
                                                                        while not exit_menu:
                                                                            # Manejar eventos
                                                                            for event in pygame.event.get():
                                                                                if event.type == pygame.QUIT:
                                                                                    sys.exit()
                                                                                elif event.type == pygame.KEYDOWN:
                                                                                    if event.key == pygame.K_UP:
                                                                                        selected_index = (selected_index - 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_DOWN:
                                                                                        selected_index = (selected_index + 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_RETURN:
                                                                                        if selected_index == 0:
                                                                                            exit_menu = True
                                                                                            exit_menu_juego = True
                                                                            
                                                                            

                                                                            # Mostrar opciones del menú
                                                                            
                                                                            for index, item in enumerate(menu_items):
                                                                                if index == selected_index:
                                                                                    display_text(
                                                                                        "> " + item, 1020, 500 + index * 100)
                                                                                else:
                                                                                    display_text(
                                                                                        item, 1020, 500 + index * 100)

                                                                            # Actualizar la pantalla
                                                                            pygame.display.update()

                                                                            # Controlar la velocidad de actualización de la pantalla
                                                                            clock.tick(60)
                                                                    
                                                                    #El juego se para i se muestra quien gano i quien perdio.
                                                                    #Tambien se muestra la opcion de volver al menu inicial.
                                                                    elif oponente_contador >= 10:
                                                                        player_text_win = game_font.render(
                                                                            "Winer!", False, light_grey )
                                                                        screen.blit(player_text_win,(340,300))
                                                                        
                                                                        oponente_text_lost = game_font.render(
                                                                            "Loser:(", False, light_grey)
                                                                        screen.blit(oponente_text_lost, (1002,300))

                                                                        ball_speed_x = 0
                                                                        ball_speed_y = 0

                                                                        menu_items = ["Volver menu inicial"]
                                                                        selected_index = 0
                                                                        exit_menu = False
                                                                        
                                                                        # Menu de puntos facil
                                                                        while not exit_menu:
                                                                            # Manejar eventos
                                                                            for event in pygame.event.get():
                                                                                if event.type == pygame.QUIT:
                                                                                    sys.exit()
                                                                                elif event.type == pygame.KEYDOWN:
                                                                                    if event.key == pygame.K_UP:
                                                                                        selected_index = (selected_index - 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_DOWN:
                                                                                        selected_index = (selected_index + 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_RETURN:
                                                                                        if selected_index == 0:
                                                                                            exit_menu = True
                                                                                            exit_menu_juego = True
                                                                            
                                                                            

                                                                            # Mostrar opciones del menú
                                                                            
                                                                            for index, item in enumerate(menu_items):
                                                                                if index == selected_index:
                                                                                    display_text(
                                                                                        "> " + item, 1020, 500 + index * 100)
                                                                                else:
                                                                                    display_text(
                                                                                        item, 1020, 500 + index * 100)

                                                                            # Actualizar la pantalla
                                                                            pygame.display.update()

                                                                            # Controlar la velocidad de actualización de la pantalla
                                                                            clock.tick(60)

                                                                    # Recargar la ventana
                                                                    pygame.display.flip()
                                                                    clock.tick(200)

                                                                pass 
                                                            
                                                            #juego en normal que termine con 20 puntos     
                                                            elif selected_index == 2:
                                                                
                                                                exit_menu_juego = False

                                                                while not exit_menu_juego:
                                                                    for event in pygame.event.get():
                                                                        if event.type == pygame.QUIT:
                                                                            pygame.quit()
                                                                            sys.exit()

                                                                        # movimiento jugador (input)

                                                                        input_jugador2(event)

                                                                    # Movimientos
                                                                    movimiento_pelota_normal()
                                                                    movimiento_jugador()
                                                                    ai_oponente()

                                                                    # Visuales
                                                                    # Color de la pantalla
                                                                    screen.fill(negro)
                                                                    pygame.draw.rect(
                                                                        screen, light_grey, jugador)
                                                                    pygame.draw.rect(
                                                                        screen, light_grey, oponente)
                                                                    pygame.draw.ellipse(
                                                                        screen, rojo, pelota,)
                                                                    pygame.draw.aaline(
                                                                        screen, light_grey, (Anchura_Pantalla/2, 0), (Anchura_Pantalla/2, Altura_Pantalla))
                                                                    pygame.draw.ellipse(
                                                                        screen, light_grey, circulo, 1)
                                                                    if score_time:
                                                                        reaparece()
                                                                    player_text = game_font.render(
                                                                        f"{jugador_contador}", False, light_grey)
                                                                    screen.blit(
                                                                        player_text, (700, 480))

                                                                    oponente_text = game_font.render(
                                                                        f"{oponente_contador}", False, light_grey)
                                                                    screen.blit(
                                                                        oponente_text, (645, 480))

                                                                    #El juego se para i se muestra quien gano i quien perdio.
                                                                    #Tambien se muestra la opcion de volver al menu inicial.
                                                                    if jugador_contador >= 20:
                                                                        player_text_win = game_font.render(
                                                                            "Loser:(", False, light_grey )
                                                                        screen.blit(player_text_win,(340,300))
                                                                        
                                                                        oponente_text_lost = game_font.render(
                                                                            "Winer!", False, light_grey)
                                                                        screen.blit(oponente_text_lost, (1002,300))

                                                                        ball_speed_x = 0
                                                                        ball_speed_y = 0

                                                                        menu_items = ["Volver menu inicial"]
                                                                        selected_index = 0
                                                                        exit_menu = False
                                                                        
                                                                        # Menu de puntos facil
                                                                        while not exit_menu:
                                                                            # Manejar eventos
                                                                            for event in pygame.event.get():
                                                                                if event.type == pygame.QUIT:
                                                                                    sys.exit()
                                                                                elif event.type == pygame.KEYDOWN:
                                                                                    if event.key == pygame.K_UP:
                                                                                        selected_index = (selected_index - 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_DOWN:
                                                                                        selected_index = (selected_index + 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_RETURN:
                                                                                        if selected_index == 0:
                                                                                            exit_menu = True
                                                                                            exit_menu_juego = True
                                                                            
                                                                            

                                                                            # Mostrar opciones del menú
                                                                            
                                                                            for index, item in enumerate(menu_items):
                                                                                if index == selected_index:
                                                                                    display_text(
                                                                                        "> " + item, 1020, 500 + index * 100)
                                                                                else:
                                                                                    display_text(
                                                                                        item, 1020, 500 + index * 100)

                                                                            # Actualizar la pantalla
                                                                            pygame.display.update()

                                                                            # Controlar la velocidad de actualización de la pantalla
                                                                            clock.tick(60)
                                                                    
                                                                    #El juego se para i se muestra quien gano i quien perdio.
                                                                    #Tambien se muestra la opcion de volver al menu inicial.
                                                                    elif oponente_contador >= 20:
                                                                        player_text_win = game_font.render(
                                                                            "Winer!", False, light_grey )
                                                                        screen.blit(player_text_win,(340,300))
                                                                        
                                                                        oponente_text_lost = game_font.render(
                                                                            "Loser:(", False, light_grey)
                                                                        screen.blit(oponente_text_lost, (1002,300))

                                                                        ball_speed_x = 0
                                                                        ball_speed_y = 0

                                                                        menu_items = ["Volver menu inicial"]
                                                                        selected_index = 0
                                                                        exit_menu = False
                                                                        
                                                                        # Menu de puntos facil
                                                                        while not exit_menu:
                                                                            # Manejar eventos
                                                                            for event in pygame.event.get():
                                                                                if event.type == pygame.QUIT:
                                                                                    sys.exit()
                                                                                elif event.type == pygame.KEYDOWN:
                                                                                    if event.key == pygame.K_UP:
                                                                                        selected_index = (selected_index - 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_DOWN:
                                                                                        selected_index = (selected_index + 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_RETURN:
                                                                                        if selected_index == 0:
                                                                                            exit_menu = True
                                                                                            exit_menu_juego = True
                                                                            
                                                                            

                                                                            # Mostrar opciones del menú
                                                                            
                                                                            for index, item in enumerate(menu_items):
                                                                                if index == selected_index:
                                                                                    display_text(
                                                                                        "> " + item, 1020, 500 + index * 100)
                                                                                else:
                                                                                    display_text(
                                                                                        item, 1020, 500 + index * 100)

                                                                            # Actualizar la pantalla
                                                                            pygame.display.update()

                                                                            # Controlar la velocidad de actualización de la pantalla
                                                                            clock.tick(60)

                                                                    # Recargar la ventana
                                                                    pygame.display.flip()
                                                                    clock.tick(200)

                                                                pass  
                                                            
                                                             #opcion volver al menu principal
                                                            
                                                            #Atras
                                                            elif selected_index == 3:
                                                                print("opcion'atras'selecionada")
                                                                exit_menu = True
                                                                break
                                                if exit_menu:
                                                    
                                                    jugador_contador = 0
                                                    oponente_contador = 0
                                
                                                    break       
                                                
                                                # Rellenar la pantalla con color negro --> Menu puntos Normal
                                                screen.fill(black)

                                                # Mostrar opciones del menú
                                                display_text2("Puntuacion", 1360/2, 700/2 - 200)
                                                for index, item in enumerate(menu_items):
                                                    if index == selected_index:
                                                        display_text(
                                                            "> " + item, 1360/2, 700/2 + index * 100)
                                                    else:
                                                        display_text(
                                                            item, 1360/2, 700/2 + index * 100)

                                                # Actualizar la pantalla
                                                pygame.display.update()

                                                # Controlar la velocidad de actualización de la pantalla
                                                clock.tick(60)
                                                                
                                        #Seleciona el juego en dificil --> Menu de puntos
                                        elif selected_index == 2:
                                            menu_items = ["5 Puntos", "10 Puntos", "20 Puntos","Atras"]
                                            selected_index = 0
                                            exit_menu = False

                                            while not exit_menu:
                                                # Manejar eventos
                                                for event in pygame.event.get():
                                                    if event.type == pygame.QUIT:
                                                        sys.exit()
                                                    elif event.type == pygame.KEYDOWN:
                                                        if event.key == pygame.K_UP:
                                                            selected_index = (selected_index - 1) % len(menu_items)
                                                        elif event.key == pygame.K_DOWN:
                                                            selected_index = (selected_index + 1) % len(menu_items)
                                                        elif event.key == pygame.K_RETURN:
                                                            
                                                            print(f"selected index:{selected_index}")
                                                            
                                                            #Juego en dificil que termine con 5 puntos
                                                            if selected_index == 0:

                                                                exit_menu_juego = False

                                                                while not exit_menu_juego:
                                                                    for event in pygame.event.get():
                                                                        if event.type == pygame.QUIT:
                                                                            pygame.quit()
                                                                            sys.exit()

                                                                        # movimiento jugador (input)

                                                                        input_jugador2(event)

                                                                    # Movimientos
                                                                    movimiento_pelota_dificil()
                                                                    movimiento_jugador()
                                                                    ai_oponente()

                                                                    # Visuales
                                                                    # Color de la pantalla
                                                                    screen.fill(negro)
                                                                    pygame.draw.rect(
                                                                        screen, light_grey, jugador)
                                                                    pygame.draw.rect(
                                                                        screen, light_grey, oponente)
                                                                    pygame.draw.ellipse(
                                                                        screen, rojo, pelota,)
                                                                    pygame.draw.aaline(
                                                                        screen, light_grey, (Anchura_Pantalla/2, 0), (Anchura_Pantalla/2, Altura_Pantalla))
                                                                    pygame.draw.ellipse(
                                                                        screen, light_grey, circulo, 1)
                                                                    if score_time:
                                                                        reaparece()

                                                                    player_text = game_font.render(
                                                                        f"{jugador_contador}", False, light_grey)
                                                                    screen.blit(
                                                                        player_text, (700, 480))

                                                                    oponente_text = game_font.render(
                                                                        f"{oponente_contador}", False, light_grey)
                                                                    screen.blit(
                                                                        oponente_text, (645, 480))

                                                                    #El juego se para i se muestra quien gano i quien perdio.
                                                                    #Tambien se muestra la opcion de volver al menu inicial.
                                                                    if jugador_contador >= 5:
                                                                        player_text_win = game_font.render(
                                                                            "Loser:(", False, light_grey )
                                                                        screen.blit(player_text_win,(340,300))
                                                                        
                                                                        oponente_text_lost = game_font.render(
                                                                            "Winer!", False, light_grey)
                                                                        screen.blit(oponente_text_lost, (1002,300))

                                                                        ball_speed_x = 0
                                                                        ball_speed_y = 0

                                                                        menu_items = ["Volver menu inicial"]
                                                                        selected_index = 0
                                                                        exit_menu = False
                                                                        
                                                                        # Menu de puntos facil
                                                                        while not exit_menu:
                                                                            # Manejar eventos
                                                                            for event in pygame.event.get():
                                                                                if event.type == pygame.QUIT:
                                                                                    sys.exit()
                                                                                elif event.type == pygame.KEYDOWN:
                                                                                    if event.key == pygame.K_UP:
                                                                                        selected_index = (selected_index - 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_DOWN:
                                                                                        selected_index = (selected_index + 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_RETURN:
                                                                                        if selected_index == 0:
                                                                                            exit_menu = True
                                                                                            exit_menu_juego = True
                                                                            
                                                                            

                                                                            # Mostrar opciones del menú
                                                                            
                                                                            for index, item in enumerate(menu_items):
                                                                                if index == selected_index:
                                                                                    display_text(
                                                                                        "> " + item, 1020, 500 + index * 100)
                                                                                else:
                                                                                    display_text(
                                                                                        item, 1020, 500 + index * 100)

                                                                            # Actualizar la pantalla
                                                                            pygame.display.update()

                                                                            # Controlar la velocidad de actualización de la pantalla
                                                                            clock.tick(60)
                                                                    
                                                                    #El juego se para i se muestra quien gano i quien perdio.
                                                                    #Tambien se muestra la opcion de volver al menu inicial.
                                                                    elif oponente_contador >= 5:
                                                                        player_text_win = game_font.render(
                                                                            "Winer!", False, light_grey )
                                                                        screen.blit(player_text_win,(340,300))
                                                                        
                                                                        oponente_text_lost = game_font.render(
                                                                            "Loser:(", False, light_grey)
                                                                        screen.blit(oponente_text_lost, (1002,300))

                                                                        ball_speed_x = 0
                                                                        ball_speed_y = 0

                                                                        menu_items = ["Volver menu inicial"]
                                                                        selected_index = 0
                                                                        exit_menu = False
                                                                        
                                                                        # Menu de puntos facil
                                                                        while not exit_menu:
                                                                            # Manejar eventos
                                                                            for event in pygame.event.get():
                                                                                if event.type == pygame.QUIT:
                                                                                    sys.exit()
                                                                                elif event.type == pygame.KEYDOWN:
                                                                                    if event.key == pygame.K_UP:
                                                                                        selected_index = (selected_index - 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_DOWN:
                                                                                        selected_index = (selected_index + 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_RETURN:
                                                                                        if selected_index == 0:
                                                                                            exit_menu = True
                                                                                            exit_menu_juego = True
                                                                            
                                                                            

                                                                            # Mostrar opciones del menú
                                                                            
                                                                            for index, item in enumerate(menu_items):
                                                                                if index == selected_index:
                                                                                    display_text(
                                                                                        "> " + item, 1020, 500 + index * 100)
                                                                                else:
                                                                                    display_text(
                                                                                        item, 1020, 500 + index * 100)

                                                                            # Actualizar la pantalla
                                                                            pygame.display.update()

                                                                            # Controlar la velocidad de actualización de la pantalla
                                                                            clock.tick(60)

                                                                    # Recargar la ventana
                                                                    pygame.display.flip()
                                                                    clock.tick(200)
                                                                pass 

                                                            #Juego en dificil que termine con 10 puntos    
                                                            elif selected_index == 1: 
                                                                
                                                                exit_menu_juego = False

                                                                while not exit_menu_juego:
                                                                    for event in pygame.event.get():
                                                                        if event.type == pygame.QUIT:
                                                                            pygame.quit()
                                                                            sys.exit()

                                                                        # movimiento jugador (input)

                                                                        input_jugador2(event)

                                                                    # Movimientos
                                                                    movimiento_pelota_dificil()
                                                                    movimiento_jugador()
                                                                    ai_oponente()

                                                                    # Visuales
                                                                    # Color de la pantalla
                                                                    screen.fill(negro)
                                                                    pygame.draw.rect(
                                                                        screen, light_grey, jugador)
                                                                    pygame.draw.rect(
                                                                        screen, light_grey, oponente)
                                                                    pygame.draw.ellipse(
                                                                        screen, rojo, pelota,)
                                                                    pygame.draw.aaline(
                                                                        screen, light_grey, (Anchura_Pantalla/2, 0), (Anchura_Pantalla/2, Altura_Pantalla))
                                                                    pygame.draw.ellipse(
                                                                        screen, light_grey, circulo, 1)
                                                                    if score_time:
                                                                        reaparece()

                                                                    player_text = game_font.render(
                                                                        f"{jugador_contador}", False, light_grey)
                                                                    screen.blit(
                                                                        player_text, (700, 480))

                                                                    oponente_text = game_font.render(
                                                                        f"{oponente_contador}", False, light_grey)
                                                                    screen.blit(
                                                                        oponente_text, (645, 480))

                                                                    #El juego se para i se muestra quien gano i quien perdio.
                                                                    #Tambien se muestra la opcion de volver al menu inicial.
                                                                    if jugador_contador >= 10:
                                                                        player_text_win = game_font.render(
                                                                            "Loser:(", False, light_grey )
                                                                        screen.blit(player_text_win,(340,300))
                                                                        
                                                                        oponente_text_lost = game_font.render(
                                                                            "Winer!", False, light_grey)
                                                                        screen.blit(oponente_text_lost, (1002,300))

                                                                        ball_speed_x = 0
                                                                        ball_speed_y = 0

                                                                        menu_items = ["Volver menu inicial"]
                                                                        selected_index = 0
                                                                        exit_menu = False
                                                                        
                                                                        # Menu de puntos facil
                                                                        while not exit_menu:
                                                                            # Manejar eventos
                                                                            for event in pygame.event.get():
                                                                                if event.type == pygame.QUIT:
                                                                                    sys.exit()
                                                                                elif event.type == pygame.KEYDOWN:
                                                                                    if event.key == pygame.K_UP:
                                                                                        selected_index = (selected_index - 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_DOWN:
                                                                                        selected_index = (selected_index + 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_RETURN:
                                                                                        if selected_index == 0:
                                                                                            exit_menu = True
                                                                                            exit_menu_juego = True
                                                                            
                                                                            

                                                                            # Mostrar opciones del menú
                                                                            
                                                                            for index, item in enumerate(menu_items):
                                                                                if index == selected_index:
                                                                                    display_text(
                                                                                        "> " + item, 1020, 500 + index * 100)
                                                                                else:
                                                                                    display_text(
                                                                                        item, 1020, 500 + index * 100)

                                                                            # Actualizar la pantalla
                                                                            pygame.display.update()

                                                                            # Controlar la velocidad de actualización de la pantalla
                                                                            clock.tick(60)
                                                                    
                                                                    #El juego se para i se muestra quien gano i quien perdio.
                                                                    #Tambien se muestra la opcion de volver al menu inicial.
                                                                    elif oponente_contador >= 10:
                                                                        player_text_win = game_font.render(
                                                                            "Winer!", False, light_grey )
                                                                        screen.blit(player_text_win,(340,300))
                                                                        
                                                                        oponente_text_lost = game_font.render(
                                                                            "Loser:(", False, light_grey)
                                                                        screen.blit(oponente_text_lost, (1002,300))

                                                                        ball_speed_x = 0
                                                                        ball_speed_y = 0

                                                                        menu_items = ["Volver menu inicial"]
                                                                        selected_index = 0
                                                                        exit_menu = False
                                                                        
                                                                        # Menu de puntos facil
                                                                        while not exit_menu:
                                                                            # Manejar eventos
                                                                            for event in pygame.event.get():
                                                                                if event.type == pygame.QUIT:
                                                                                    sys.exit()
                                                                                elif event.type == pygame.KEYDOWN:
                                                                                    if event.key == pygame.K_UP:
                                                                                        selected_index = (selected_index - 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_DOWN:
                                                                                        selected_index = (selected_index + 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_RETURN:
                                                                                        if selected_index == 0:
                                                                                            exit_menu = True
                                                                                            exit_menu_juego = True
                                                                            
                                                                            

                                                                            # Mostrar opciones del menú
                                                                            
                                                                            for index, item in enumerate(menu_items):
                                                                                if index == selected_index:
                                                                                    display_text(
                                                                                        "> " + item, 1020, 500 + index * 100)
                                                                                else:
                                                                                    display_text(
                                                                                        item, 1020, 500 + index * 100)

                                                                            # Actualizar la pantalla
                                                                            pygame.display.update()

                                                                            # Controlar la velocidad de actualización de la pantalla
                                                                            clock.tick(60)

                                                                    # Recargar la ventana
                                                                    pygame.display.flip()
                                                                    clock.tick(200)
                                                                pass  
                                                            
                                                            #juego en dificil que termine con 20 puntos
                                                            elif selected_index == 2:
                                                                
                                                                exit_menu_juego = False
                                                                while not exit_menu_juego:
                                                                    for event in pygame.event.get():
                                                                        if event.type == pygame.QUIT:
                                                                            pygame.quit()
                                                                            sys.exit()

                                                                        # movimiento jugador (input)

                                                                        input_jugador2(event)

                                                                    # Movimientos
                                                                    movimiento_pelota_dificil()
                                                                    movimiento_jugador()
                                                                    ai_oponente()

                                                                    # Visuales
                                                                    # Color de la pantalla
                                                                    screen.fill(negro)
                                                                    pygame.draw.rect(
                                                                        screen, light_grey, jugador)
                                                                    pygame.draw.rect(
                                                                        screen, light_grey, oponente)
                                                                    pygame.draw.ellipse(
                                                                        screen, rojo, pelota,)
                                                                    pygame.draw.aaline(
                                                                        screen, light_grey, (Anchura_Pantalla/2, 0), (Anchura_Pantalla/2, Altura_Pantalla))
                                                                    pygame.draw.ellipse(
                                                                        screen, light_grey, circulo, 1)
                                                                    if score_time:
                                                                        reaparece()

                                                                    player_text = game_font.render(
                                                                        f"{jugador_contador}", False, light_grey)
                                                                    screen.blit(
                                                                        player_text, (700, 480))

                                                                    oponente_text = game_font.render(
                                                                        f"{oponente_contador}", False, light_grey)
                                                                    screen.blit(
                                                                        oponente_text, (645, 480))
                                                                    
                                                                    #El juego se para i se muestra quien gano i quien perdio.
                                                                    #Tambien se muestra la opcion de volver al menu inicial.
                                                                    if jugador_contador >= 10:
                                                                        player_text_win = game_font.render(
                                                                            "Loser:(", False, light_grey )
                                                                        screen.blit(player_text_win,(340,300))
                                                                        
                                                                        oponente_text_lost = game_font.render(
                                                                            "Winer!", False, light_grey)
                                                                        screen.blit(oponente_text_lost, (1002,300))

                                                                        ball_speed_x = 0
                                                                        ball_speed_y = 0

                                                                        menu_items = ["Volver menu inicial"]
                                                                        selected_index = 0
                                                                        exit_menu = False
                                                                        
                                                                        # Menu de puntos facil
                                                                        while not exit_menu:
                                                                            # Manejar eventos
                                                                            for event in pygame.event.get():
                                                                                if event.type == pygame.QUIT:
                                                                                    sys.exit()
                                                                                elif event.type == pygame.KEYDOWN:
                                                                                    if event.key == pygame.K_UP:
                                                                                        selected_index = (selected_index - 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_DOWN:
                                                                                        selected_index = (selected_index + 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_RETURN:
                                                                                        if selected_index == 0:
                                                                                            exit_menu = True
                                                                                            exit_menu_juego = True
                                                                            
                                                                            

                                                                            # Mostrar opciones del menú
                                                                            
                                                                            for index, item in enumerate(menu_items):
                                                                                if index == selected_index:
                                                                                    display_text(
                                                                                        "> " + item, 1020, 500 + index * 100)
                                                                                else:
                                                                                    display_text(
                                                                                        item, 1020, 500 + index * 100)

                                                                            # Actualizar la pantalla
                                                                            pygame.display.update()

                                                                            # Controlar la velocidad de actualización de la pantalla
                                                                            clock.tick(60)
                                                                    
                                                                    #El juego se para i se muestra quien gano i quien perdio.
                                                                    #Tambien se muestra la opcion de volver al menu inicial.
                                                                    elif oponente_contador >= 10:
                                                                        player_text_win = game_font.render(
                                                                            "Winer!", False, light_grey )
                                                                        screen.blit(player_text_win,(340,300))
                                                                        
                                                                        oponente_text_lost = game_font.render(
                                                                            "Loser:(", False, light_grey)
                                                                        screen.blit(oponente_text_lost, (1002,300))

                                                                        ball_speed_x = 0
                                                                        ball_speed_y = 0

                                                                        menu_items = ["Volver menu inicial"]
                                                                        selected_index = 0
                                                                        exit_menu = False
                                                                        
                                                                        # Menu de puntos facil
                                                                        while not exit_menu:
                                                                            # Manejar eventos
                                                                            for event in pygame.event.get():
                                                                                if event.type == pygame.QUIT:
                                                                                    sys.exit()
                                                                                elif event.type == pygame.KEYDOWN:
                                                                                    if event.key == pygame.K_UP:
                                                                                        selected_index = (selected_index - 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_DOWN:
                                                                                        selected_index = (selected_index + 1) % len(menu_items)
                                                                                    elif event.key == pygame.K_RETURN:
                                                                                        if selected_index == 0:
                                                                                            exit_menu = True
                                                                                            exit_menu_juego = True
                                                                            
                                                                            

                                                                            # Mostrar opciones del menú
                                                                            
                                                                            for index, item in enumerate(menu_items):
                                                                                if index == selected_index:
                                                                                    display_text(
                                                                                        "> " + item, 1020, 500 + index * 100)
                                                                                else:
                                                                                    display_text(
                                                                                        item, 1020, 500 + index * 100)

                                                                            # Actualizar la pantalla
                                                                            pygame.display.update()

                                                                            # Controlar la velocidad de actualización de la pantalla
                                                                            clock.tick(60)

                                                                    # Recargar la ventana
                                                                    pygame.display.flip()
                                                                    clock.tick(200)
                                                                pass 
                                                
                                                             #opcion volver al menu principal
                                                            
                                                            # Atras
                                                            elif selected_index == 3:
                                                                print("opcion'atras'selecionada")
                                                                exit_menu = True
                                                                break
                                                if exit_menu:
                                                    jugador_contador = 0
                                                    oponente_contador = 0
                                
                                                    break       
                                                
                                                # Rellenar la pantalla con color negro --> Menu puntos Dificil
                                                screen.fill(black)

                                                # Mostrar opciones del menú
                                                display_text2("Puntuacion", 1360/2, 700/2 - 200)
                                                for index, item in enumerate(menu_items):
                                                    if index == selected_index:
                                                        display_text(
                                                            "> " + item, 1360/2, 700/2 + index * 100)
                                                    else:
                                                        display_text(
                                                            item, 1360/2, 700/2 + index * 100)

                                                # Actualizar la pantalla
                                                pygame.display.update()

                                                # Controlar la velocidad de actualización de la pantalla
                                                clock.tick(60)
                                        
                                        #opcion volver al menu principal
                                        elif selected_index == 3:
                                            print("opcion'atras'selecionada")
                                            exit_menu = True
                                            break
                            if exit_menu:
                                
                                break
                            
                            # Rellenar la pantalla con color negro
                            screen.fill(black)

                            # Mostrar opciones del menú
                            display_text2("Dificultad", 1360/2, 700/2 - 200)
                            for index, item in enumerate(menu_items):
                                if index == selected_index:
                                    display_text(
                                        "> " + item, 1360/2, 700/2 + index * 100)
                                else:
                                    display_text(
                                        item, 1360/2, 700/2 + index * 100)

                            # Actualizar la pantalla
                            pygame.display.update()

                            # Controlar la velocidad de actualización de la pantalla
                            clock.tick(60)
                    
                    #Escoje Ver creditos
                    elif selected_index == 1:
                        
                        menu_items = ["Atras"]
                        selected_index = 0
                        exit_menu = False
                        
                        while not exit_menu:
                            # Manejar eventos
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    sys.exit()
                                elif event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_UP:
                                        selected_index = (
                                            selected_index - 1) % len(menu_items)
                                    elif event.key == pygame.K_DOWN:
                                        selected_index = (
                                            selected_index + 1) % len(menu_items)
                                    elif event.key == pygame.K_RETURN:
                                        if selected_index == 0:
                                            # Volver al menú principal
                                            exit_menu = True

                            # Rellenar la pantalla con color negro
                            screen.fill(black)

                            # Mostrar opciones del menú
                            dispaly_text_multiline(
                                "Creditos \nCreador del juego: Oscar Garcia Fernan. \nFecha del juego: 24/4/2023 \nTutor a cargo: Pau Duaso \nApoyo Emocional: Hugo Revilla,Carlos Pastran \nMaria Carvajal, Sousana Ziati", 700, 100)

                            for index, item in enumerate(menu_items):
                                if index == selected_index:
                                    display_text(
                                        "> " + item, 1360/2, 700/2+200 + index * 100)
                                else:
                                    display_text(
                                        item, 1360/2, 700/2 + index * 100)

                            # Actualizar la pantalla
                            pygame.display.update()

                            # Controlar la velocidad de actualización de la pantalla
                            clock.tick(60)
                            pass
                    
                    #Escoje Cerrar Juego
                    elif selected_index == 2:
                        sys.exit()

        # Rellenar la pantalla con color negro
        screen.fill(black)

        # Mostrar opciones del menú
        display_text2("Pin Pong", 1360/2, 700/2 - 200)
        if True:
            for index, item in enumerate(menu_items):
                if index == selected_index:
                    display_text("> " + item, 1360/2, 700/2 + index * 100)
                else:
                    display_text(item, 1360/2, 700/2 + index * 100)

        # Actualizar la pantalla
        pygame.display.update()

        # Controlar la velocidad de actualización de la pantalla
        clock.tick(60)


# Llamar a la función del menú del juego
game_menu()


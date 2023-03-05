
# juego de hundir la flota
turno_jugador = True
while True:
    if turno_jugador:
        x = int(input("Ingresa una fila: "))
        y = int(input("Ingresa una columna: "))
        if disparar(tablero_con_barcos, x, y):
            print("¡Has hundido un barco!")
            if todos_barcos_hundidos(tablero_con_barcos):
                print("¡Felicidades, has ganado!")
                break  # Termina el juego
            turno_jugador = True  # Has acertado, otro turno
        else:
            turno_jugador = False  # Has fallado, otro turno
    else:
        if disparar_maquina(tablero):
            print("La máquina ha hundido uno de tus barcos.")
            if todos_barcos_hundidos(tablero_con_barcos):
                print("¡Has perdido!")
                break  # Termina el juego
        turno_jugador = True  # Turno del jugador
import random

def simular_melate():
    # Definimos el rango del juego (1 al 56)
    rango_numeros = range(1, 57)
    
    # Preguntamos al usuario si desea escribir el sus numeros o que la maquina los escriba por el
    print("\n--- Bienvenido al Juego Melate ---")
    print("1) Escribir tus números")
    print("2) Generar números aleatorios")
    
    opcion = 0
    while True:
        try:
            opcion = int(input("\n¿Qué opción eliges?: "))
            if 1 <= opcion <= 2:
                break
            else:
                print("Error: Elige 1 o 2.")
        except ValueError:
            print("Error: Ingresa un número válido.")


    mis_numeros = []

    if opcion == 1:
        # PARTE 3: El usuario elige
        print("\nPor favor ingresa tus 6 números del 1 al 56")
        for i in range(1, 7):
            while True:
                try:
                    value = int(input(f"Ingresa el número {i}: "))
                    if 1 <= value <= 56:
                        if value not in mis_numeros:
                            mis_numeros.append(value)
                            break
                        else:
                            print("Ese número ya lo elegiste.")
                    else:
                        print("Error: Entre 1 y 56.")
                except ValueError:
                    print("Error: Ingresa un número.")
    
    else:
        # PARTE 4: La máquina elige
        print("\nGenerando tus números aleatorios...")
        mis_numeros = random.sample(rango_numeros, 6)

    # --- EL SORTEO (Esto ocurre siempre, sin importar la opción) ---
    # Sacamos 7 números de un solo golpe
    esferas_sorteadas = random.sample(rango_numbers, 7)

    # Los primeros 6 son los "Naturales"
    naturales = esferas_sorteadas[:6] 

    # El que sobra (el séptimo) es el "Adicional"
    adicional = esferas_sorteadas[6]
    
    aciertos = set(mis_numeros).intersection(set(naturales))
    num_aciertos = len(aciertos)
    
    print("-" * 30)
    print(f"Tus números: {sorted(mis_numeros)}")
    print(f"Sorteo oficial: {sorted(naturales)}")
    print(f"Número adicional: {adicional}")
    print(f"Aciertos: {num_aciertos}")
    print("-" * 30)

    if num_aciertos == 6:
        print("¡ERES MILLONARIO!")
    elif num_aciertos == 5 and adicional in mis_numeros:
        print("¡Segundo lugar!")
    elif num_aciertos >= 2:
        print("Ganaste un premio menor.")
    else:
        print("Sigue participando.")

simular_melate()
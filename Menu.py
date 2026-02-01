import random

def simular_melate():
    # 1. Definimos el rango del juego (1 al 56)
    rango_numeros = range(1, 57)

    # 2. Pedimos tus 6 números de la suerte
    # Usamos random.sample para simular una elección aleatoria sin repetir
    mis_numeros = random.sample(rango_numeros, 6)
    
    # 3. El sorteo oficial (6 esferas naturales + 1 adicional)
    # Seleccionamos 7 números en total
    esferas_sorteadas = random.sample(rango_numeros, 7)
    
    naturales = esferas_sorteadas[:6] # Los primeros 6
    adicional = esferas_sorteadas[6]  # El último es el adicional
    
    # 4. Comparar (Intersección de conjuntos)
    # Esto busca qué números están en ambos grupos
    aciertos = set(mis_numeros).intersection(set(naturales))
    num_aciertos = len(aciertos)
    
    # 5. Mostrar resultados
    print(f"Tus números: {sorted(mis_numeros)}")
    print(f"Números naturales del sorteo: {sorted(naturales)}")
    print(f"Número adicional: {adicional}")
    print(f"\n¡Tuviste {num_aciertos} aciertos!")
    
    if num_aciertos == 6:
        print("¡ERES MILLONARIO!")
    elif num_aciertos == 5 and adicional in mis_numeros:
        print("¡Ganaste el segundo lugar!")
    elif num_aciertos >= 2:
        print("Ganaste un premio menor.")
    else:
        print("Sigue participando.")

# Ejecutamos la función
simular_melate()    
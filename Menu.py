import random

# --- CLASE PADRE: El motor general de cualquier sorteo ---
class SorteoBase:
    def __init__(self):
        self.rango = range(1, 57)
        self.mis_numeros = []
        self.ganadores = []

    def elegir_numeros_usuario(self):
        print("\nPor favor ingresa tus 6 números del 1 al 56")
        self.mis_numeros = [] # Limpiamos
        for i in range(1, 7):
            while True:
                try:
                    value = int(input(f"Ingresa el número {i}: "))
                    if 1 <= value <= 56 and value not in self.mis_numeros:
                        self.mis_numeros.append(value)
                        break
                    else:
                        print("Error: Número fuera de rango o ya elegido.")
                except ValueError:
                    print("Error: Ingresa un número válido.")

    def generar_numeros_aleatorios(self):
        print("\nGenerando tus números aleatorios...")
        self.mis_numeros = random.sample(self.rango, 6)

    def comparar(self, lista_ganadores):
        # Lógica común de intersección de conjuntos
        return set(self.mis_numeros).intersection(set(lista_ganadores))

# --- CLASE HIJA: Reglas específicas de Melate ---
class JuegoMelate(SorteoBase):
    def __init__(self):
        super().__init__() # Inicializa lo del padre
        self.adicional = None

    def ejecutar_sorteo_oficial(self):
        # Melate saca 7 esferas
        esferas = random.sample(self.rango, 7)
        self.ganadores = esferas[:6]
        self.adicional = esferas[6]

    def mostrar_resultados(self):
        aciertos = self.comparar(self.ganadores)
        num_aciertos = len(aciertos)
        
        print("-" * 30)
        print(f"Tus números: {sorted(self.mis_numeros)}")
        print(f"Sorteo oficial: {sorted(self.ganadores)}")
        print(f"Número adicional: {self.adicional}")
        print(f"Aciertos: {num_aciertos}")
        print("-" * 30)

        if num_aciertos == 6:
            print("¡ERES MILLONARIO!")
        elif num_aciertos == 5 and self.adicional in self.mis_numeros:
            print("¡Segundo lugar (5 naturales + adicional)!")
        elif num_aciertos >= 2:
            print("Ganaste un premio menor.")
        else:
            print("Sigue participando.")
            
# --- CLASE HIJA: Reglas para la Revancha ---
class JuegoRevancha(SorteoBase):
    def __init__(self):
        super().__init__()
        self.nombre = "Revancha"
        self.costo = 10 

    def ejecutar_sorteo_oficial(self):
        # A diferencia del Melate, la Revancha NO tiene número adicional
        self.ganadores = random.sample(self.rango, 6)

    def mostrar_resultados(self):
        aciertos = self.comparar(self.ganadores)
        num_aciertos = len(aciertos)
        
        print(f"\n--- Resultados {self.nombre} ---")
        print(f"Tus números: {sorted(self.mis_numeros)}")
        print(f"Sorteo: {sorted(self.ganadores)}")
        print(f"Aciertos: {num_aciertos}")
        
        if num_aciertos >= 2:
            print(f"¡Ganaste un premio en {self.nombre}!")
        else:
            print(f"No hubo suerte en {self.nombre}.")


# --- CLASE HIJA: Revanchita  ---
class JuegoRevanchita(SorteoBase):
    def __init__(self):
        super().__init__()
        self.nombre = "Revanchita"
        self.costo = 5

    def ejecutar_sorteo_oficial(self):
        # Sorteo de 6 números (sin adicional)
        self.ganadores = random.sample(self.rango, 6)

    def mostrar_resultados(self):
        aciertos = self.comparar(self.ganadores)
        num_aciertos = len(aciertos)
        print(f"\n--- Resultados {self.nombre} ---")
        print(f"Sorteo: {sorted(self.ganadores)}")
        print(f"Aciertos: {num_aciertos}")
        
        if num_aciertos == 6:
            print("¡GANASTE EL PREMIO MAYOR DE REVANCHITA!")
        else:
            print("En Revanchita solo se gana con los 6 aciertos.")
            
            
def simular_melate():
    # 1. Menú
    print("\n--- BIENVENIDO AL SORTEO ---")
    print("1) Solo Melate ($15)")
    print("2) Melate + Revancha ($25)")
    print("3) Melate + Revancha + Revanchita ($30)")
    
    while True:
        modalidad = input("\nSelecciona tu modalidad: ")
        if modalidad in ["1", "2", "3"]:
            break
        print("Opción no válida.")

    # 2. Creación de los objetos según la elección
    juegos_a_jugar = [JuegoMelate()]
    
    if modalidad == "2":
        juegos_a_jugar.append(JuegoRevancha())
    elif modalidad == "3":
        juegos_a_jugar.append(JuegoRevancha())
        juegos_a_jugar.append(JuegoRevanchita())

    # 3. Entrada de números
    print("\n1) Escribir tus números")
    print("2) Generar números aleatorios")
    
    opcion_input = input("¿Cómo quieres tus números?: ")
    
    primer_juego = juegos_a_jugar[0]
    if opcion_input == "1":
        primer_juego.elegir_numeros_usuario()
    else:
        primer_juego.generar_numeros_aleatorios()
    
    mis_numeros = primer_juego.mis_numeros

    # 4. EJECUCIÓN
    print("\n" + "="*40)
    print("INICIANDO SORTEOS OFICIALES")
    print("="*40)

    for juego in juegos_a_jugar:
        juego.mis_numeros = mis_numeros 
        juego.ejecutar_sorteo_oficial()
        juego.mostrar_resultados()
        
if __name__ == "__main__":
    simular_melate()
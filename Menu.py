import random

# --- CLASE PADRE: El motor general de cualquier sorteo ---
class SorteoBase:
    def __init__(self):
        self.rango = range(1, 57)
        self.mis_numeros = []
        self.ganadores = []

    def elegir_numeros_usuario(self):
        print("\nPor favor ingresa tus 6 números del 1 al 56")
        self.mis_numeros = [] # Limpiamos por si acaso
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
            
            
            
def simular_melate():
    juego = JuegoMelate() # Creamos el objeto
    
    print("\n--- Bienvenido al Juego Melate (Versión POO) ---")
    print("1) Escribir tus números")
    print("2) Generar números aleatorios")
    
    while True:
        try:
            opcion = int(input("\n¿Qué opción eliges?: "))
            if opcion == 1:
                juego.elegir_numeros_usuario()
                break
            elif opcion == 2:
                juego.generar_numeros_aleatorios()
                break
            else:
                print("Error: Elige 1 o 2.")
        except ValueError:
            print("Error: Ingresa un número válido.")

    # Ejecutamos la lógica del objeto
    juego.ejecutar_sorteo_oficial()
    juego.mostrar_resultados()

if __name__ == "__main__":
    simular_melate()
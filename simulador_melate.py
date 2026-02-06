import random

# ============================================================
# CLASE PADRE: SorteoBase
# ------------------------------------------------------------
# Esta clase define la estructura y comportamiento general
# que comparten todos los juegos de sorteo (Melate, Revancha,
# Revanchita).
# ============================================================
class SorteoBase:
    def __init__(self):
        # Rango de números permitidos en el sorteo (1 al 56)
        self.rango = range(1, 57)
        # Lista donde se almacenan los números del usuario
        self.mis_numeros = []
        # Lista de números ganadores del sorteo
        self.ganadores = []

    def elegir_numeros_usuario(self):
        """
        Permite al usuario ingresar manualmente 6 números.
        Valida que estén dentro del rango y que no se repitan.
        """
        print("\nPor favor ingresa tus 6 números del 1 al 56")
        self.mis_numeros = []  # Limpia números previos

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
        """
        Genera automáticamente 6 números aleatorios sin repetirse.
        """
        print("\nGenerando tus números aleatorios...")
        self.mis_numeros = random.sample(self.rango, 6)

    def comparar(self, lista_ganadores):
        """
        Compara los números del usuario con los números ganadores
        usando intersección de conjuntos.
        """
        return set(self.mis_numeros).intersection(set(lista_ganadores))


# ============================================================
# CLASE HIJA: JuegoMelate
# ------------------------------------------------------------
# Implementa las reglas específicas del juego Melate,
# incluyendo el número adicional.
# ============================================================
class JuegoMelate(SorteoBase):
    def __init__(self):
        super().__init__()  # Inicializa atributos del padre
        self.adicional = None  # Número adicional del sorteo

    def ejecutar_sorteo_oficial(self):
        """
        Genera el sorteo oficial de Melate.
        Se extraen 7 números: 6 ganadores y 1 adicional.
        """
        esferas = random.sample(self.rango, 7)
        self.ganadores = esferas[:6]
        self.adicional = esferas[6]

    def mostrar_resultados(self):
        """
        Muestra los resultados del sorteo Melate
        y determina el tipo de premio.
        """
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


# ============================================================
# CLASE HIJA: JuegoRevancha
# ------------------------------------------------------------
# Implementa las reglas del juego Revancha.
# No cuenta con número adicional.
# ============================================================
class JuegoRevancha(SorteoBase):
    def __init__(self):
        super().__init__()
        self.nombre = "Revancha"
        self.costo = 10

    def ejecutar_sorteo_oficial(self):
        """
        Genera el sorteo oficial de Revancha
        con 6 números ganadores.
        """
        self.ganadores = random.sample(self.rango, 6)

    def mostrar_resultados(self):
        """
        Muestra los resultados del sorteo Revancha
        e indica si hubo premio.
        """
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


# ============================================================
# CLASE HIJA: JuegoRevanchita
# ------------------------------------------------------------
# Implementa las reglas del juego Revanchita.
# Solo se gana con 6 aciertos.
# ============================================================
class JuegoRevanchita(SorteoBase):
    def __init__(self):
        super().__init__()
        self.nombre = "Revanchita"
        self.costo = 5

    def ejecutar_sorteo_oficial(self):
        """
        Genera el sorteo oficial de Revanchita
        con 6 números ganadores.
        """
        self.ganadores = random.sample(self.rango, 6)

    def mostrar_resultados(self):
        """
        Muestra los resultados del sorteo Revanchita.
        """
        aciertos = self.comparar(self.ganadores)
        num_aciertos = len(aciertos)

        print(f"\n--- Resultados {self.nombre} ---")
        print(f"Sorteo: {sorted(self.ganadores)}")
        print(f"Aciertos: {num_aciertos}")

        if num_aciertos == 6:
            print("¡GANASTE EL PREMIO MAYOR DE REVANCHITA!")
        else:
            print("En Revanchita solo se gana con los 6 aciertos.")


# ============================================================
# FUNCIÓN PRINCIPAL
# ------------------------------------------------------------
# Controla el flujo general del programa:
# menú, selección de modalidad, ejecución de sorteos
# ============================================================
def simular_melate():
    # Menú principal
    print("\n--- BIENVENIDO AL SORTEO ---")
    print("1) Solo Melate ($15)")
    print("2) Melate + Revancha ($25)")
    print("3) Melate + Revancha + Revanchita ($30)")

    while True:
        modalidad = input("\nSelecciona tu modalidad: ")
        if modalidad in ["1", "2", "3"]:
            break
        print("Opción no válida.")

    # Creación de los juegos según la modalidad
    juegos_a_jugar = [JuegoMelate()]

    if modalidad == "2":
        juegos_a_jugar.append(JuegoRevancha())
    elif modalidad == "3":
        juegos_a_jugar.append(JuegoRevancha())
        juegos_a_jugar.append(JuegoRevanchita())

    # Elección de números del usuario
    print("\n1) Escribir tus números")
    print("2) Generar números aleatorios")

    opcion_input = input("¿Cómo quieres tus números?: ")

    primer_juego = juegos_a_jugar[0]
    if opcion_input == "1":
        primer_juego.elegir_numeros_usuario()
    else:
        primer_juego.generar_numeros_aleatorios()

    # Se reutilizan los mismos números para todos los juegos
    mis_numeros = primer_juego.mis_numeros

    # Ejecución de sorteos
    print("\n" + "=" * 40)
    print("INICIANDO SORTEOS OFICIALES")
    print("=" * 40)

    for juego in juegos_a_jugar:
        juego.mis_numeros = mis_numeros
        juego.ejecutar_sorteo_oficial()
        juego.mostrar_resultados()


# Punto de entrada del programa
if __name__ == "__main__":
    simular_melate()

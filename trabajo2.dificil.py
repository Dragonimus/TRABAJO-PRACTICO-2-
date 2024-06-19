class MisionEspacial:
    def __init__(self):
        pass

    def calcular_combinaciones(self, total_personas, tamano_equipo):
        """
        Calcula el número total de combinaciones posibles de equipos de astronautas.

        Args:
            total_personas (int): Número total de personas disponibles.
            tamano_equipo (int): Tamaño del equipo requerido.

        Returns:
            int: Número total de combinaciones posibles de equipos.
        """
        from math import factorial
        combinaciones = factorial(total_personas) / (factorial(tamano_equipo) * factorial(total_personas - tamano_equipo))
        return int(combinaciones)

if __name__ == "__main__":
    mision = MisionEspacial()

    # Nivel dificil
    total_personas = int(input("Ingrese el número total de personas disponibles: "))
    tamano_equipo = int(input("Ingrese el tamaño del equipo requerido: "))
    total_combinaciones = mision.calcular_combinaciones(total_personas, tamano_equipo)
    print("El número total de combinaciones posibles de equipos de astronautas es:", total_combinaciones)

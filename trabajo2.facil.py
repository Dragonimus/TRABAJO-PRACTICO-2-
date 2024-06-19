class MisionEspacial:
    def __init__(self):
        pass

    def calcular_tiempo_viaje(self, distancia, velocidad):
        """
        Calcula el tiempo de viaje a la Luna.

        Args:
            distancia (float): Distancia entre la Tierra y la Luna en kilómetros.
            velocidad (float): Velocidad de la nave espacial en kilómetros por hora.

        Returns:
            float: Tiempo de viaje en horas.
        """
        tiempo_viaje = distancia / velocidad
        return tiempo_viaje

    def calcular_area_lunar(self, base, altura):
        """
        Calcula el área de una superficie lunar.

        Args:
            base (float): Longitud de la base de la superficie lunar.
            altura (float): Altura de la superficie lunar.

        Returns:
            float: Área de la superficie lunar.
        """
        area = base * altura
        return area

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

    # Nivel fácil
    distancia_tierra_luna = float(input("Ingrese la distancia entre la Tierra y la Luna (en kilómetros): "))
    velocidad_nave = float(input("Ingrese la velocidad de la nave espacial (en kilómetros por hora): "))
    tiempo_total = mision.calcular_tiempo_viaje(distancia_tierra_luna, velocidad_nave)
    print("El tiempo de viaje a la Luna es de aproximadamente", tiempo_total, "horas.")

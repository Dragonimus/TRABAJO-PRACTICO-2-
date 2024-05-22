class MisionEspacial:
    def __init__(self):
        pass

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

if __name__ == "__main__":
    mision = MisionEspacial()

    # Nivel intermedio
    base_superficie = float(input("Ingrese la longitud de la base de la superficie lunar (en kilómetros): "))
    altura_superficie = float(input("Ingrese la altura de la superficie lunar (en kilómetros): "))
    area_total = mision.calcular_area_lunar(base_superficie, altura_superficie)
    print("El área de la superficie lunar es de", area_total, "kilómetros cuadrados.")

class Artefacto:
    def __init__(self, descripcion):
        self.descripcion = descripcion

    def determinar_tipo(self):
        """
        Determina si el artefacto es un tesoro oculto o un adorno decorativo.

        Returns:
            str: El tipo de artefacto (tesoro oculto o adorno decorativo).
        """
        if "joya mágica" in self.descripcion.lower() or "antiguo mapa del tesoro" in self.descripcion.lower():
            return "tesoro oculto"
        else:
            return "adorno decorativo"

if __name__ == "__main__":
    descripcion_artefacto = input("Los jóvenes aventureros han encontrado un artefacto en la Ciudad Encantada. Por favor, describe el artefacto: ")

    artefacto = Artefacto(descripcion_artefacto)
    tipo_artefacto = artefacto.determinar_tipo()

    print(f"El artefacto encontrado es un {tipo_artefacto}.")

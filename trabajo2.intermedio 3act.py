class MensajeEnigmatico:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def clasificar(self):
        """
        Clasifica el mensaje enigmático como una pista útil o una distracción peligrosa.

        Returns:
            str: La clasificación del mensaje (pista útil o distracción peligrosa).
        """
        if "tesoro" in self.mensaje.lower() or "pista" in self.mensaje.lower():
            return "pista útil"
        else:
            return "distracción peligrosa"

if __name__ == "__main__":
    mensaje_enigmatico = input("Los jóvenes aventureros han encontrado un mensaje enigmático tallado en una antigua estatua. Por favor, escribe el mensaje: ")

    mensaje = MensajeEnigmatico(mensaje_enigmatico)
    clasificacion_mensaje = mensaje.clasificar()

    print(f"El mensaje enigmático se clasifica como una {clasificacion_mensaje}.")

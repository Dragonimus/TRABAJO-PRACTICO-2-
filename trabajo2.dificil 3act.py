import random

def obtener_adivinanza():
    """
    Obtiene aleatoriamente una adivinanza y su respuesta de una lista predefinida.

    Returns:
        tuple: Una tupla que contiene la adivinanza y su respuesta.
    """
    adivinanzas = [
        ("Tiene ojos y no puede ver, tiene un cuerpo y no puede caminar. ¿Qué es?", "Una botella"),
        ("Blanco por dentro, verde por fuera. Si quieres que te lo diga, espera.", "La pera"),
        ("Un sombrero tengo, sin copa ni visera, y cuando me necesitas en tu mano me paseas.", "El paraguas"),
        # Agrega más adivinanzas según sea necesario
    ]
    return random.choice(adivinanzas)

def jugar_juego():
    """
    Inicia el juego de adivinanzas.
    """
    print("¡Bienvenidos al juego de adivinanzas para abrir la puerta mágica!")
    print("Responde correctamente a las adivinanzas para avanzar en tu búsqueda.\n")

    adivinanzas_restantes = 3
    while adivinanzas_restantes > 0:
        adivinanza, respuesta = obtener_adivinanza()
        print(f"Adivinanza: {adivinanza}")
        respuesta_usuario = input("¿Cuál es tu respuesta? ").strip().lower()

        if respuesta_usuario == respuesta.lower():
            print("¡Respuesta correcta! Avanzas al siguiente desafío.\n")
            adivinanzas_restantes -= 1
            if adivinanzas_restantes == 0:
                print("¡Has superado todos los desafíos! La puerta mágica se abre.")
        else:
            print("Respuesta incorrecta. Intenta de nuevo.\n")

if __name__ == "__main__":
    jugar_juego()

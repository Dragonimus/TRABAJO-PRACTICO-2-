def hechizo_suficientemente_fuerte(potencia_hechizo, resistencia_enemigo):
    """
    Comprueba si la potencia del hechizo es suficiente para derrotar al enemigo.

    Args:
        potencia_hechizo (float): La potencia del hechizo.
        resistencia_enemigo (float): El nivel de resistencia del enemigo.

    Returns:
        bool: True si el hechizo es lo suficientemente fuerte, False en caso contrario.
    """
    return potencia_hechizo >= resistencia_enemigo

if __name__ == "__main__":
    potencia_hechizo = float(input("Ingresa la potencia del hechizo: "))
    resistencia_enemigo = float(input("Ingresa el nivel de resistencia del enemigo: "))

    if hechizo_suficientemente_fuerte(potencia_hechizo, resistencia_enemigo):
        print("¡El hechizo es lo suficientemente fuerte para derrotar al enemigo!")
    else:
        print("El hechizo no es lo suficientemente fuerte para derrotar al enemigo.")

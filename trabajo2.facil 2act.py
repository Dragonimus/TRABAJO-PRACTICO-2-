def describir_personaje(nombre_personaje, cantidad_pociones):
    """
    Muestra un mensaje describiendo al personaje y la cantidad de pociones mágicas que posee.

    Args:
        nombre_personaje (str): El nombre del personaje.
        cantidad_pociones (int): La cantidad de pociones mágicas que posee el personaje.
    """
    print(f"{nombre_personaje} es un valiente aventurero que posee {cantidad_pociones} pociones mágicas.")

if __name__ == "__main__":
    nombre_personaje = input("¡Bienvenido a tu aventura mágica! Por favor, ingresa el nombre de tu personaje: ")
    cantidad_pociones = int(input("Ingresa el número de pociones mágicas que posee tu personaje: "))

    describir_personaje(nombre_personaje, cantidad_pociones)

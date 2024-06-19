def factorial(n):
    """
    Calcula el factorial de un número entero.

    Args:
        n (int): El número entero.

    Returns:
        int: El factorial de n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def calcular_combinaciones(num_personajes):
    """
    Calcula el número total de combinaciones posibles de personajes para formar un equipo.

    Args:
        num_personajes (int): El número total de personajes disponibles.

    Returns:
        int: El número total de combinaciones posibles de personajes.
    """
    return factorial(num_personajes)

if __name__ == "__main__":
    num_personajes = int(input("Ingresa el número total de personajes disponibles: "))

    total_combinaciones = calcular_combinaciones(num_personajes)

    print(f"El número total de combinaciones posibles de personajes para formar un equipo es: {total_combinaciones}")

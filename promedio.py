"""Programa que calcula el promedio de una lista de números."""


def calcular_promedio(numeros):
    """Calcula el promedio de una lista de números.

    Suma todos los valores de la lista y divide el resultado
    para la cantidad de elementos.

    Args:
        numeros (list): Lista de valores enteros o decimales.

    Returns:
        float: Promedio de los valores de la lista.

    Raises:
        ValueError: Si la lista está vacía.

    Example:
        >>> calcular_promedio([8, 9, 10])
        9.0
    """
    # Se valida la lista para evitar una división para cero
    if not numeros:
        raise ValueError("La lista no puede estar vacía")

    # Se suman los valores y se divide para la cantidad de elementos
    return sum(numeros) / len(numeros)


if __name__ == "__main__":
    # Prueba de la función con las notas de un estudiante
    notas = [8.5, 9, 7.75, 10, 9.25]
    print("Notas:", notas)
    print(f"Promedio: {calcular_promedio(notas):.2f}")

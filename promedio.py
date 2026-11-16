"""Cálculo del promedio de una lista de números.

Módulo desarrollado para la actividad de Cultura Digital y Sociedad
(UNACH). Muestra cómo documentar una función con docstrings siguiendo
la convención PEP 257 y el formato de Google.

Uso desde la terminal:
    python promedio.py
"""


def calcular_promedio(numeros):
    """Calcula el promedio (media aritmética) de una lista de números.

    El promedio se obtiene sumando todos los valores y dividiendo el
    resultado para la cantidad de elementos.

    Args:
        numeros (list[int | float]): Lista con los valores numéricos.

    Returns:
        float: Promedio de los valores de la lista.

    Raises:
        ValueError: Si la lista está vacía, porque no se puede dividir
            para cero.
        TypeError: Si algún elemento no es un número.

    Examples:
        >>> calcular_promedio([8, 9, 10])
        9.0
        >>> calcular_promedio([7.5, 8.25])
        7.875
    """
    # Validación 1: una lista vacía provocaría una división para cero.
    if len(numeros) == 0:
        raise ValueError("La lista está vacía; no se puede calcular el promedio.")

    # Validación 2: todos los elementos deben ser int o float
    # (se excluye bool, que en Python es un subtipo de int).
    for valor in numeros:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError(f"El valor {valor!r} no es un número.")

    # Cálculo: suma total dividida para la cantidad de elementos.
    return sum(numeros) / len(numeros)


if __name__ == "__main__":
    # Ejemplo: calificaciones de un estudiante sobre 10 puntos.
    calificaciones = [8.5, 9.0, 7.75, 10, 9.25]
    resultado = calcular_promedio(calificaciones)
    print(f"Calificaciones: {calificaciones}")
    print(f"Promedio: {resultado:.2f}")

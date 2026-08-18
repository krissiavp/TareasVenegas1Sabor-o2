def filtrar_vocales(cadena, bandera):
    """
    Filtra las vocales o consonantes de una cadena.

    Retorna:
        codigo_estado, resultado
    """

    # Verifica que cadena sea un string
    if not isinstance(cadena, str):
        return -100, None

    # Verifica que cadena no esté vacía
    if cadena == "":
        return -300, None

    # Verifica que solo contenga letras
    if not cadena.isalpha():
        return -200, None

    # Verifica que no tenga más de 30 caracteres
    if len(cadena) > 30:
        return -400, None

    # Verifica que bandera sea booleana
    if not isinstance(bandera, bool):
        return -500, None

    vocales = "aeiouAEIOU"
    resultado = ""

    if bandera:
        for letra in cadena:
            if letra in vocales:
                resultado += letra
    else:
        for letra in cadena:
            if letra not in vocales:
                resultado += letra

    return 0, resultado


def encontrar_extremos(lista_numeros):
    """
    Encuentra el valor mínimo y máximo de una lista numérica.

    Retorna:
        codigo_estado, minimo, maximo
    """

    # Verifica que el parámetro sea una lista
    if not isinstance(lista_numeros, list):
        return -600, None, None

    # Verifica que la lista no esté vacía
    if len(lista_numeros) == 0:
        return -800, None, None

    # Verifica que no tenga más de 15 elementos
    if len(lista_numeros) > 15:
        return -900, None, None

    # Verifica que todos los elementos sean números
    for numero in lista_numeros:
        if isinstance(numero, bool):
            return -700, None, None

        if not isinstance(numero, (int, float)):
            return -700, None, None

    minimo = min(lista_numeros)
    maximo = max(lista_numeros)

    return 0, minimo, maximo

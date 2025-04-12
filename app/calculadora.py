# app/calculadora.py
"""
Módulo que contiene las operaciones básicas de una calculadora.

Este módulo proporciona funciones para realizar operaciones matemáticas básicas:
- Suma
- Resta
- Multiplicación
- División

Todas las funciones aceptan números de punto flotante como entrada y devuelven
el resultado como un número de punto flotante.
"""

def sumar(a, b):
    """
    Realiza la suma de dos números.

    Args:
        a (float): Primer número a sumar.
        b (float): Segundo número a sumar.

    Returns:
        float: El resultado de la suma a + b.
    """
    return a + b


def restar(a, b):
    """
    Realiza la resta de dos números.

    Args:
        a (float): Número del que se resta.
        b (float): Número que se resta.

    Returns:
        float: El resultado de la resta a - b.
    """
    return a - b


def multiplicar(a, b):
    """
    Realiza la multiplicación de dos números.

    Args:
        a (float): Primer factor.
        b (float): Segundo factor.

    Returns:
        float: El resultado de la multiplicación a * b.
    """
    return a * b


def dividir(a, b):
    """
    Realiza la división de dos números.

    Args:
        a (float): Dividendo.
        b (float): Divisor.

    Returns:
        float: El resultado de la división a / b.

    Raises:
        ZeroDivisionError: Si el divisor (b) es cero.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b

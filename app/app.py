# app/app.py
"""
Módulo principal de la aplicación de calculadora web.

Este módulo implementa una aplicación web Flask que proporciona una
interfaz para realizar operaciones matemáticas básicas. La aplicación
maneja solicitudes GET y POST, procesa los datos del formulario y
muestra los resultados.

La aplicación incluye manejo de errores para:
- Entradas no numéricas
- División por cero
- Operaciones no válidas
"""

from flask import Flask, render_template, request
from .calculadora import sumar, restar, multiplicar, dividir

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Maneja las solicitudes GET y POST para la página principal de la
    calculadora.

    Esta función procesa los números y la operación enviados a través
    del formulario, realiza el cálculo correspondiente y devuelve el
    resultado.

    Returns:
        str: Una plantilla HTML renderizada con el resultado del
        cálculo o None si no se ha realizado ninguna operación.

    Raises:
        ValueError: Si los números ingresados no son válidos.
        ZeroDivisionError: Si se intenta dividir por cero.
    """
    resultado = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operacion = request.form["operacion"]

            if operacion == "sumar":
                resultado = sumar(num1, num2)
            elif operacion == "restar":
                resultado = restar(num1, num2)
            elif operacion == "multiplicar":
                resultado = multiplicar(num1, num2)
            elif operacion == "dividir":
                resultado = dividir(num1, num2)
            else:
                resultado = "Operación no válida"
        except ValueError:
            resultado = "Error: Introduce números válidos"
        except ZeroDivisionError:
            resultado = "Error: No se puede dividir por cero"

    return render_template("index.html", resultado=resultado)

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":  # pragma: no cover
    # Quita debug=True para producción
    app.run(port=5000, host="0.0.0.0")

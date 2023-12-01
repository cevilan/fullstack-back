"""
Módulo app
"""
from flask import Flask, request, redirect, Response
import persistencia

app=Flask (__name__)

@app.route("/pizza",methods=['POST'])

def pizza():
    """
    Function pizza
    """
    nombre=request.form.get("nombre")
    apellidos=request.form.get("apellidos")
    persistencia.guardar_pedido(nombre,apellidos)
    return redirect("http://localhost/fullstack/solicita_pedido.html", code=302)

@app.route("/checksize",methods=['POST'])

def checksize():
    """
    Comprueba disponibilidad de un tamaño de pizza.
    """
    tamano=request.form.get("tamano")
    
    if tamano=='S':
        mensaje="No disponible"
    else:
        mensaje="Disponible"
    
    return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})

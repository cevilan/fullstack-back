from flask import Flask, request, redirect
import persistencia

app=Flask (__name__)

@app.route("/pizza",methods=['POST'])  

def pizza():
    nombre=request.form.get("nombre") 
    apellidos=request.form.get("apellidos") 
    
    persistencia.guardar_pedido(nombre,apellidos)
    
    return redirect("http://localhost/actividad-M1-U1/solicita_pedido.html", code=302)

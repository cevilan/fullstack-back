"""
Módulo persistencia
"""
def guardar_pedido(nombre, apellidos):
    """
    Function guardar_pedido
    """
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write(nombre + " " + apellidos + "\n")
        file.close()
        
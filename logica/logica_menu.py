def listar_menu(menu):
    return menu


def buscar_productos(menu, texto):
    texto = texto.lower()
    return [
        productos for productos in menu
        if texto in productos["nombre"].lower()
        or texto in productos["categoria"].lower()
    ]


def obtener_productos_por_id(menu, id_producto):
    for producto in menu:
        if producto["id"] == id_producto:
            return producto
    return None



        

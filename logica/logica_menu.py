def listar_menu(menu):
    return menu


def buscar_platos(menu, texto):
    texto = texto.lower()
    return [
        plato for plato in menu
        if texto in plato["nombre"].lower()
        or texto in plato["categoria"].lower()
    ]


def obtener_plato_por_id(menu, id_plato):
    for plato in menu:
        if plato["id"] == id_plato:
            return plato
    return None



        

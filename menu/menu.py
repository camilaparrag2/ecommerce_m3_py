import questionary


def mostrar_menu_principal():
    return questionary.select(
        "Bienvenido/a a tu Ecommerce",
        choices=[
            "Ver catalogo de productos",
            "Buscar producto",
            "Agregar producto al carrito",
            "Ver carrito",
            "Vaciar carrito",
            "Salir"
        ]
    ).ask()


def pedir_texto(mensaje):
    return questionary.text(mensaje).ask()


def pedir_numero(mensaje):
    valor = questionary.text(mensaje).ask()
    return int(valor)


def mostrar_productos(productos):
    if not productos:
        print("No hay resultados")
        return

    for p in productos:
        print(f"{p['id']} - {p['nombre']} (${p['precio']}) [{p['categoria']}]")
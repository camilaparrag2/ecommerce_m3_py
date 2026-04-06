def agregar_al_carrito(carrito, productos, cantidad):
    carrito.append({
        "productos": productos,
        "cantidad": cantidad
    })


def calcular_total(carrito):
    total = 0
    for item in carrito:
        total += item["productos"]["precio"] * item["cantidad"]
    return total


def vaciar_carrito(carrito):
    carrito.clear()







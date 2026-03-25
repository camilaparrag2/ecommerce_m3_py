def agregar_al_carrito(carrito, plato, cantidad):
    carrito.append({
        "plato": plato,
        "cantidad": cantidad
    })


def calcular_total(carrito):
    total = 0
    for item in carrito:
        total += item["plato"]["precio"] * item["cantidad"]
    return total


def vaciar_carrito(carrito):
    carrito.clear()







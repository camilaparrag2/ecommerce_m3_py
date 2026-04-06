from menu.menu import mostrar_menu_principal, mostrar_productos, pedir_texto, pedir_numero
from logica.logica_menu import listar_menu, buscar_productos, obtener_productos_por_id
from data.menu_data import menu
from logica.logica_carrito import agregar_al_carrito, calcular_total, vaciar_carrito
import os



def main():
    carrito = []
    while True:
        
        opcion = mostrar_menu_principal()
        os.system('cls' if os.name == 'nt' else 'clear')
        

        if opcion == "Ver catalogo de productos":
            productos = listar_menu(menu)
            mostrar_productos(productos)
            
        elif opcion == "Buscar producto":
            texto = pedir_texto("Agrega un producto al carro")
            resultado = buscar_productos(menu, texto)
            mostrar_productos(resultado)

        elif opcion == "Agregar producto al carrito": 
            id_productos = pedir_numero("ID del producto:")
            cantidad = pedir_numero("cantidad de productos: ")
            
            if cantidad <= 0:
                print("Debes ingresar una cantidad válida.")
                continue
            
            producto = obtener_productos_por_id(menu, id_productos)
            
            if not producto:
                print("¡Producto no encontrado!")
                
            else:
                agregar_al_carrito(carrito, producto, cantidad)
                print("¡Agregado al carrito!")


        elif opcion == "Ver carrito":
        
            if not carrito:
                print("Sin carrito que mostrar.")
            
            total = calcular_total(carrito)

            for productos in carrito:
                p = productos["productos"]
                c = productos["cantidad"]
                print(f"productos: {p['nombre']} - cantidad: {c}")
            print(f"el total de tu compra es de: {total}")
        
        elif opcion == "Vaciar carrito":
            vaciar_carrito(carrito)
            print("¡Carrito vacio!")
              
        elif opcion == "Salir":
            print("Saliendo...")
            break


if __name__ == "__main__":
    main()












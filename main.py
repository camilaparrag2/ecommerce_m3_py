from menu.menu import mostrar_menu_principal, mostrar_platos, pedir_texto,pedir_numero
from logica.logica_menu import listar_menu, buscar_platos, obtener_plato_por_id
from data.menu_data import menu
from logica.logica_carrito import agregar_al_carrito, calcular_total, vaciar_carrito
import os



def main():
    carrito = []
    while True:
        
        opcion = mostrar_menu_principal()
        os.system('cls' if os.name == 'nt' else 'clear')
        

        if opcion == "Ver menú":
            platos = listar_menu(menu)
            mostrar_platos(platos)
            
        elif opcion == "Buscar plato":
            texto = pedir_texto("que quieres comer!! ")
            resultado = buscar_platos(menu, texto)
            mostrar_platos(resultado)

        elif  opcion == "Agregar al carrito": 
            id_plato = pedir_numero("ID del plato:")
            cantidad = pedir_numero("cantidad de productos: ")

            if cantidad <= 0:
                print("para agregar al carrito tiene que pasarce una cantidad!!")

            plato = obtener_plato_por_id(menu, id_plato)

            if not plato:
                print("sin platos!!!")

            agregar_al_carrito(carrito, plato, cantidad)
            print("agregado al carrito!!")


        elif opcion == "Ver carrito":
        
            if not carrito:
                print("sin carrito que mostrar")
            
            total = calcular_total(carrito)

            for plato in carrito:
                p = plato["plato"]
                c = plato["cantidad"]
                print(f"plato: {p["nombre"]} - catidad: {c}")
            print(f"el total de tu compra es de: {total}")
        
        elif opcion == "Vaciar carrito":
            vaciar_carrito(carrito)
            print("carrito borrado!!!!!")
        
        elif opcion == "Salir":
            print("saliendo de la app!!")
            break


if __name__ == "__main__":
    main()












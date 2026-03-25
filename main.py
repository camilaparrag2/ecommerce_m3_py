from menu.menu import mostrar_menu_principal, mostrar_platos, pedir_texto
from logica.logica_menu import listar_menu, buscar_platos
from data.menu_data import menu

def main():
    carrito = []
    while True:

        opcion = mostrar_menu_principal()

        if opcion == "Ver menú":
            platos = listar_menu(menu)
            mostrar_platos(platos)
            
        elif opcion == "Buscar plato":
            texto = pedir_texto("que quieres comer!! ")
            resultado = buscar_platos(menu, texto)
            mostrar_platos(resultado)

        elif  opcion == "Agregar al carrito": 
            pass 

        



main()












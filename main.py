# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 07:17:56 2023

@author: Erick
"""

# selec = input(print('***************************************************',
#       '\n***************************************************',
#       '\n             +++++ USAC CINEMA +++++'
#       '\n'
#       '\nMENU DE OPCIONES'
#       '\n'
#       '\n1. Iniciar sesión',
#       '\n2. Registrar usuario',
#       '\n3. Ver listado de peliculas',
#       '\n'
#       '\n***************************************************',
#       '\n***************************************************'))

    
    
# def iniciar_sesion():
#     pass
    
# def regis_usuario():
#     pass

# def ver_peliculas():
#     pass


from peliculas import Pelicula
from administradores import Administrador
from clientes import Cliente


def menu_principal():
    print('\n***************************************************',
          '\n***************************************************',
          '\n             +++++ USAC CINEMA +++++'
          '\n'
          '\n*MENU DE OPCIONES*'
          '\n'
          '\n1. Iniciar sesión',
          '\n2. Registrar usuario',
          '\n3. Ver listado de peliculas',
          '\n4. Salir del programa'
          '\n'
          '\n***************************************************',
          '\n***************************************************')
    
def menu_iniciar_sesion():
    print('\n\n->INICIAR SESION:',
          '\n       1. Administrador',
          '\n       2. Cliente',
          '\n       3. Regresar al menú principal')

def imprimir_menu_principal():
    while True:
        menu_principal()
        opcion_principal = input('\nSeleccione una opción del 1 al 4: ')
        
        if opcion_principal == '1':
            imprimir_iniciar_sesion()
        elif opcion_principal == '2':      
            print("->REGISTRAR USUARIO")
        elif opcion_principal == '3':
            print("\n\n->LISTADO DE PELICULAS")
            pelicula = Pelicula()
            pelicula.lista()
            input()
        elif opcion_principal == '4':
            print('\n\n->SALIENDO DEL PROGRAMA')
            break
        else:
            print("\n\n*Opción inválida*")  
            
def imprimir_iniciar_sesion():
    while True:
        menu_iniciar_sesion()
        opcion_iniciar_sesion = input('\nSeleccione una opción del 1 al 3: ')
        
        if opcion_iniciar_sesion == '1':
            # print('-> Opción 1')         
            usuario_admin = Administrador("admin1@usac.edu.com", "contrasena1")
            usuario_admin.iniciar_sesion_admin()
        elif opcion_iniciar_sesion == '2':
            # print('-> Opción 2')
            usuario_cliente = Cliente("cliente1@usac.edu.com", "contrasena2")
            usuario_cliente.iniciar_sesion_cliente()
        elif opcion_iniciar_sesion == '3':
            break
        else:
            print("\n\n*Opción inválida*")            
    # selec()

imprimir_menu_principal()

# usuario_ejemplo = Administrador("administrador1@usac.edu.com", "contrasena1")
# usuario_ejemplo.iniciar_sesion()








# def mostrar_menu_principal():
#     print("Menú Principal")
#     print("1. Opción 1")
#     print("2. Opción 2")
#     print("3. Opción 3")
#     print("4. Salir")

# def mostrar_submenu():
#     print("Menú Secundario")
#     print("a. Opción A")
#     print("b. Opción B")
#     print("c. Opción C")
#     print("r. Regresar al menú principal")

# def ejecutar_menu_principal():
#     while True:
#         mostrar_menu_principal()
#         opcion_principal = input("Seleccione una opción: ")

#         if opcion_principal == "1":
#             print("Ha seleccionado la Opción 1")
#         elif opcion_principal == "2":
#             print("Ha seleccionado la Opción 2")
#         elif opcion_principal == "3":
#             ejecutar_submenu()
#         elif opcion_principal == "4":
#             print("Saliendo del programa...")
#             break
#         else:
#             print("Opción inválida. Por favor, seleccione nuevamente.")

# def ejecutar_submenu():
#     while True:
#         mostrar_submenu()
#         opcion_submenu = input("Seleccione una opción: ")

#         if opcion_submenu == "a":
#             print("Ha seleccionado la Opción A")
#         elif opcion_submenu == "b":
#             print("Ha seleccionado la Opción B")
#         elif opcion_submenu == "c":
#             print("Ha seleccionado la Opción C")
#         elif opcion_submenu == "r":
#             break
#         else:
#             print("Opción inválida. Por favor, seleccione nuevamente.")

# ejecutar_menu_principal()









    
# def suma(a, b):
#     return a + b

# def resta(a, b):
#     return a - b

# def multiplicacion(a, b):
#     return a * b

# def division(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return "Error: División por cero"

# def calcular():
#     print("Calculadora")
#     print("1. Suma")
#     print("2. Resta")
#     print("3. Multiplicación")
#     print("4. División")
#     print("5. Salir")

#     opcion = input("Seleccione una opción: ")

#     if opcion == "5":
#         return

#     num1 = float(input("Ingrese el primer número: "))
#     num2 = float(input("Ingrese el segundo número: "))

#     if opcion == "1":
#         resultado = suma(num1, num2)
#         print("El resultado de la suma es:", resultado)
#     elif opcion == "2":
#         resultado = resta(num1, num2)
#         print("El resultado de la resta es:", resultado)
#     elif opcion == "3":
#         resultado = multiplicacion(num1, num2)
#         print("El resultado de la multiplicación es:", resultado)
#     elif opcion == "4":
#         resultado = division(num1, num2)
#         print("El resultado de la división es:", resultado)
#     else:
#         print("Opción inválida")

#     # print()
#     calcular()

# calcular()


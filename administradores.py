# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 07:58:01 2023

@author: Erick
"""

# from usuarioLES import Usuario
from crud import Crud
from usuarioLES import Usuario

class Administrador:
    def __init__(self, correo_admin, contrasena_admin):
        self.correo_admin = correo_admin
        self.contrasena_admin = contrasena_admin
            
    def iniciar_sesion_admin(self):
        correo = input("\n\nIngrese su correo electrónico: ")
        contrasena = input("Ingrese su contraseña: ")
        
        if correo == self.correo_admin and contrasena == self.contrasena_admin:
            print('\n¡BIENVENIDO! \|/ INICIO DE SESION EXITOSO \|/')
            while True:
                print('\n           1. Gestionar usuarios',
                      '\n           2. Gestionar categoraias y peliculas',
                      '\n           3. Gestionar salas'
                      '\n           4. Cerrar sesión')
            
                opcion_admin = input('\nSeleccione una opción del 1 al 4: ')
                if opcion_admin == '1':
                    print('-> GESTIONAR usuarios')
                    crud = Crud
                    crud.imprimir_crud(self)
                    lista_usuarios = Usuario()
                    lista_usuarios.CargarXML(1)
                    lista_usuarios.Imprimir()
                    input('\n')
                elif opcion_admin == '2':      
                    print('->GESTIONAR CATEGORIAS Y PELICULAS')
                elif opcion_admin == '3':
                    print('-> GESTIONAR SALAS')
                    crud = Crud
                    crud.imprimir_crud(self)
                    input('\n')
                elif opcion_admin == '4':
                    print('\n\n->SESION CERRADA')
                    break
                else:
                    print('\n\n*Opción inválida*')
        else:
            print("\n-----Correo o contraseña incorrectos-----")

# Crear un usuario de ejemplo
# usuario_ejemplo = Administrador("administrador1@usac.edu.com", "contrasena1")

# Iniciar sesión
# usuario_ejemplo.iniciar_sesion()




# # Base de datos de usuarios registrados (solo para fines de demostración)
# usuarios_registrados = {
#     'usuario1@example.com': 'contrasena1',
#     'usuario2@example.com': 'contrasena2',
#     'usuario3@example.com': 'contrasena3'
# }


# def iniciar_sesion():
#     print("Inicio de sesión")
#     correo = input("Ingrese su correo electrónico: ")
#     contrasena = input("Ingrese su contraseña: ")

#     if correo in usuarios_registrados and usuarios_registrados[correo] == contrasena:
#         print("Inicio de sesión exitoso. ¡Bienvenido!")
#         # Aquí puedes agregar la lógica adicional que deseas ejecutar después del inicio de sesión exitoso
#     else:
#         print("Credenciales inválidas. Por favor, inténtelo nuevamente.")

# iniciar_sesion()

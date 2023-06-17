# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 07:58:01 2023

@author: Erick
"""

# from usuarioLES import Usuario
from crud import Crud

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

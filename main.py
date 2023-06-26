import funciones as fn
flag = True 
ls =[]
ln =[]
lse =[]
while flag:
    print("1.- Registrar asignatura")
    print("2.- Agregar alumno a la asignatura")
    print("3.- Mostrar asignatura")
    print("4.- Salir")
    
    try:
        opc = int(input("ingrese opcion: "))
        
        if opc == 1:
            
            validar_sigla = False
            while validar_sigla == False:
                sigla = input("ingrese sigla de la asignatura: ")
                validar_sigla = fn.validar_sigla(sigla)
                if validar_sigla == False:
                    print("ingrese seccion valida ")
            
         
            validar_nombre_asign = False
            while validar_nombre_asign == False:
                nom = input("Ingrese nombre de la asignatura: ")
                validar_nombre_asign = fn.validar_nombre_asign(nom)
                if validar_nombre_asign == False:
                    print("Ingrese un nombre válido para la asignatura")

            validar_seccion = False
            while validar_seccion == False:
                sec = input("Ingrese sección: ")
                validar_seccion = fn.validar_seccion(sec)
                if validar_seccion == False:
                    print("Ingrese un número válido para la sección")
       
            fn.agregar_lista(sigla, nom, sec, ls, ln, lse)
        
        
        
    except:
        print("ingrese valor valido")
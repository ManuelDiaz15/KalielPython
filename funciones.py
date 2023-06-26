def validar_sigla(sigla):
    if len(sigla) == 7:
        return  True
    
    else:
        return False
    
def validar_nombre_asign(nom):
    if len(nom) >= 5:
        return True
    else:
        return False
    
def validar_seccion(sec):
    if len(sec) == 3:
        return True 
    else:
        return False 
    
def agregar_lista(sigla, nom, sec, ls, ln, lse):
    
    ls.append(sigla)
    ln.append(nom)
    lse.append(sec)
    
    print("se agregaron los valores a las listas ")
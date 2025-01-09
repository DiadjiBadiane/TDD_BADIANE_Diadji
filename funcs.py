#exercice 1

#fonction qui renvoie les 3 plus grandes valeurs d' une liste d' entier
def max_listes(liste_entiers):
    nouvelle_liste = sorted(liste_entiers)
    return(nouvelle_liste[len(nouvelle_liste) - 3:len(nouvelle_liste)])

#fonction qui renvoie true si un nombre est premier, false sinon
def nombre_premier(nombre):
    if (nombre <= 1):
        return False
    
    elif(nombre == 2):
        return True
    
    elif(nombre % 2 == 0):
        return False
    
    else:
        for k in range (3, int(nombre ** 0.5) + 1, 2):
            if nombre % k == 0:
                return False
        return True
    

#fonction qui renvoie si une suite est arithmétique
def est_arithmetique(liste):
    pass

            
    
    


if __name__ == '__main__':
    max_listes([1, 2, 3, 4, 5, 6])
    max_listes([6, 5, 4, 3, 2, 1])
    max_listes([462, 427, 404, 332, 838])
    max_listes([128, 854, 102, 710, 44])
    max_listes([301, 250, 552, 384, 474])
    nombre_premier(1)
    nombre_premier(2)
    nombre_premier(3)
    nombre_premier(7)
    nombre_premier(17)
    nombre_premier(4)
    nombre_premier(9)
    nombre_premier(15)
    nombre_premier(0)
    nombre_premier(-7)

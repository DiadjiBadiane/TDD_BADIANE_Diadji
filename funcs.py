#exercice 1

#fonction qui renvoie les 3 plus grandes valeurs d' une liste d' entier
def max_listes(liste_entiers):
    nouvelle_liste = sorted(liste_entiers)
    return(nouvelle_liste[len(nouvelle_liste) - 3:len(nouvelle_liste)])


def nombre_premier(nombre):
    pass

if __name__ == '__main__':
    max_listes([1, 2, 3, 4, 5, 6])
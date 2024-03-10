## Importation des modules
import turtle
import random
from functools import reduce

## Définition des fonctions

#def generer_liste_num_formes():
#    return [random.randint(1, 6) for i in range(5)]

def generer_formes_avec_couleurs():
    couleurs = ['red', 'blue', 'green', 'yellow', 'orange', 'purple'] 
    formes_avec_couleurs = [(random.randint(1, 6), random.choice(couleurs)) for _ in range(5)]
    return formes_avec_couleurs

nombres_couleurs_aleatoires = generer_formes_avec_couleurs()
print(nombres_couleurs_aleatoires)

def forme(parametres):
    def fonction_sortie(position):
        '''
        Dessine une forme géométrique en fonction du paramètre n
        @param entrée position : (int, int), position de la forme sous la forme (absisse, ordonnée)
        @param entrée n : int, numéro de la forme, nombre de côtés si n>=3
        '''
        turtle.color(parametres[1])
        turtle.penup()
        turtle.goto(position[0], position[1])
        turtle.pendown()

        if parametres[0] == 1:
            turtle.circle(50)
        elif parametres[0] == 2:
            for i in range(5):
                turtle.forward(50)
                turtle.left(180 - 180 / 5)
        elif parametres[0] >= 3:
            for i in range(parametres[0]):
                turtle.forward(50)
                turtle.left(360 / parametres[0])
                
    return fonction_sortie


## Programme principal

# configuration de la tortue
turtle.speed(0)
#turtle.pensize(2)

# exécution du dessin
pentagone = forme(5)
cercle = forme(1)

#pentagone((10,200))
#cercle((-50, 0))

# fin du dessin
#turtle.done()


liste_formes = list(map(lambda x: forme(x), nombres_couleurs_aleatoires))
print(liste_formes)

#liste_formes[0]((100, 200))
#liste_formes[1]((-100, 100))
#liste_formes[2]((100, -200))

#for i in range(len(liste_formes)):
#    position = (random.randint(-300,300), random.randint(-300,300))
#   liste_formes[i](position)

ffc = lambda acc, x: acc((random.randint(-300,300), random.randint(-300,300)))if acc != None else x((random.randint(-300,300), random.randint(-300,300)))
ffc2 = lambda x: x((random.randint(-300,300), random.randint(-300,300)))
pooo = reduce(ffc, liste_formes)
#print(pooo)



turtle.done()
#pos = (random.randint(-300,300), random.randint(-300,300))
#ffcprint = lambda x, pos: x(pos)
#liste_formes_print = functools.reduce(ffcprint, liste_formes)
## Importation des modules

import functools


## Déclaration des classes


## Déclaration des fonctions


## Programme principal

paragraphe = """
En inforatique, la programmation purement fonctionnelle est un paradigme de programmation — un style de construction de la structure et des éléments des programmes informatiques — qui considère toutes les opérations comme l'évaluation de fonctions mathématiques.

L'état et les objets immuables sont généralement modélisés à l'aide d'une logique temporelle, en tant que variables explicites représentant l'état du programme à chaque étape de son exécution : l'état d'une variable est transmis en tant que paramètre d'entrée d'une fonction de transformation d'état, qui renvoie l'état mis à jour en tant que partie de sa valeur de retour. Ce style gère les modifications d'état sans perdre la transparence référentielle des expressions du programme.

La programmation fonctionnelle pure consiste à s'assurer que les fonctions dans un paradigme fonctionnel, ne dépendent que de leurs arguments, indépendamment de tout état global ou local. Un sous-programme fonctionnel pur ne peut voir que les changements d'état des variables incluses dans sa portée.
"""

liste_phrases = paragraphe.split('.')
#print(liste_phrases)

# print(liste_phrases[0].count('fonction'))

f_compte = lambda phrase: phrase.count('fonction')
liste_occurences = list(map(f_compte, liste_phrases))
#print(liste_occurences)

f_somme = lambda acc, x: acc + x
total = functools.reduce(f_somme, liste_occurences)
print(total)

f_filtre = lambda phrase: 'programmation' in phrase
liste_filtree = list(filter(f_filtre, liste_phrases))
#print(liste_filtree)

liste_personnes = [{'prenom': 'Marie', 'taille': 160},
 {'prenom': 'Isla', 'taille': 82},
 {'prenom': 'Samüël'},
 {'prenom': 'Bernard'},
 {'prenom': 'Julie', 'taille': 190},
 {'prenom': 'Isabelle', 'taille': 157},
 {'prenom': 'Lucas'},
 {'prenom': 'Karine', 'taille': 162}]

#9/ Dictionnaires dans une liste

#affiche chaque dico ou la taille est rensignée
fo_filtre = lambda x: 'taille' in x
perso_taille = list(filter(fo_filtre, liste_personnes))
print(perso_taille)


#compte la tille des dico
fo_compte = lambda liste: len(liste)
liste_compte = list(map(fo_compte, liste_personnes))
print(liste_compte)

#extrait la liste des tailles
fonc_tailles = lambda x: x['taille']
tailles = list(map(fonc_tailles, perso_taille))
print(tailles)

#Moyenne tailles
sommes_moy = lambda x, y: x + y
somme_tailles = functools.reduce(lambda x, y: x + y, tailles)
print(somme_tailles/ len(perso_taille))








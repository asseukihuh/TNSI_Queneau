#Importation des modules

'''1) La recherche dichotomique consiste a rechercher un element dans un tableau trié en comparant
la valeur a chaque fois au milieu de la liste a l'element recherché'''

#Declaration des fonctions


def dichotomie(tab, x):
    #Cas 1 : Si la liste est vide
    '''
    zfZEFZgzqgqeb
    '''
    if len(tab) == 0:
        return False, 1
    #Cas 2 : x n'est pas contenu dans le tableau
    if (x < tab[0]) or (x > tab[len(tab) - 1]):
        return False, 2
    #Cas 3 : La valeur est comprise dans la tableau
    debut = 0
    fin = len(tab) -1
    while debut <= fin:
        m = len(tab)/2
        if x == tab[m]:
            return True
        if x > tab[m]:     
            debut = m + 1
        else:
            fin = m - 1
    return True

#Recherche dichotomique par recurrence de https://github.com/anonymecrasher

def recur_dichotomie(tab, x):
    """
    tab : tableau trie dans l'ordre croissant
    x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    if len(tab) == 0:
        return False,1
    if (x < tab[0]) or (x > tab[len(tab)-1]):
        return False, 2
    
    m =  (len(tab)-1) // 2
    if x == tab[m-1]:
        return True
    elif  x > tab[m]:
        return recur_dichotomie(tab[m + 1:],x)
    else:
        return recur_dichotomie(tab[:m - 1],x)
    
    return False    

#Programme principal


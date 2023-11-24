class Pile:
    def __init__(self):
        self.tableau = ()

    def est_vide(self):
        return len(self.tableau) == 0

    def empiler(self, valeur):
        self.tableau += (valeur,)

    def depiler(self):
        if self.est_vide():
            return('la liste est vide')
        valeur = self.tableau[-1]
        self.tableau = self.tableau[:-1]
        print('Le tuple dépilé est :', tuple(self.tableau))
        return valeur

    def sommet(self):
        if self.est_vide():
            return('la liste est vide')
        return self.tableau[-1]

    def longueur(self):
        n = 0
        if self.est_vide():
            return n
        else:
            piletemp = Pile()
            while self.est_vide() == False:
                piletemp.empiler(self.depiler())
                n = n + 1
            while piletemp.est_vide() == False:
                self.empiler(piletemp.depiler())
            return n
            
    

    def pile_en_tuple(self):
        return tuple(self.tableau)


pile = Pile()
print(pile.est_vide())

pile.empiler(10)
pile.empiler(20)
pile.empiler(30)

print("Le sommet de la pile est :", pile.sommet())
print("la taille de la pile est :", pile.longueur())
print("La pile en tuple :", pile.pile_en_tuple())

valeur_depilee = pile.depiler()
print("Valeur dépile :", valeur_depilee)
print("La pile après dépilement :", pile.pile_en_tuple())

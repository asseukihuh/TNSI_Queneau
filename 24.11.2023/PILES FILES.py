class Pile:
    def __init__(self):
        self.tableau = ()

    def est_vide(self):
        return len(self.tableau) == 0

    def empiler(self, valeur):
        self.tableau += (valeur,)

    def depiler(self):
        if self.est_vide():
            raise IndexError("La pile est vide, impossible de dépiler.")
        valeur = self.tableau[-1]
        self.tableau = self.tableau[:-1]
        return valeur

    def sommet(self):
        if self.est_vide():
            raise IndexError("La pile est vide, pas de sommet.")
        return self.tableau[-1]

    def longueur(self):
        return len(self.tableau)

    def pile_en_tuple(self):
        return tuple(reversed(self.tableau))


pile = Pile()
print(pile.est_vide())

pile.empiler(10)
pile.empiler(20)
pile.empiler(30)

print("Sommet de la pile :", pile.sommet())
print("Taille de la pile :", pile.longueur())
print("La pile en tuple :", pile.pile_en_tuple())

valeur_depilee = pile.depiler()
print("Valeur dépile :", valeur_depilee)
print("La pile après dépilement :", pile.pile_en_tuple())

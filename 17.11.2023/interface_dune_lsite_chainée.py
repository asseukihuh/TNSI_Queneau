class Maillon():
    def __init__(self, valeur=None, suivant=None):
        self.valeur = valeur
        self.suivant = suivant

class Liste_chainee():
    def __init__(self):
        self.tete = None

    def est_vide(self):
        return self.tete is None

    def ajouter_element_queue(self, valeur):
        if self.est_vide():
            self.tete = Maillon(valeur)
        else:
            maillon = self.tete
            while maillon.suivant is not None:
                maillon = maillon.suivant
            maillon.suivant = Maillon(valeur)

    def list(self):
        a = []
        maillon = self.tete
        while maillon is not None:
            a.append(maillon.valeur)
            maillon = maillon.suivant
        return a

    def longueur(self):
        temp = 0
        maillon = self.tete
        while maillon is not None:
            temp += 1
            maillon = maillon.suivant
        return temp

    def extrait_element(self, position):
        assert not self.est_vide(), "LA LISTE EST VIDE !!!!!!!!!!!!!!!"
        assert position < self.longueur(), "LA VALEUR EST TROP GRANDE !!!!"
        
        temp = 0
        maillon = self.tete
        while temp < position:
            maillon = maillon.suivant
            temp += 1
        return maillon.valeur

    def ajouter_element_tete(self, valeur):
        self.tete = Maillon(valeur, self.tete)

    def supprimer_element_queue(self):
        if self.longueur() < 2:
            self.tete = None
        else:
            maillon = self.tete
            while maillon.suivant.suivant is not None:
                maillon = maillon.suivant
            maillon.suivant = None

    def supprimer_element_tete(self):
        if not self.est_vide():
            self.tete = self.tete.suivant

    def inserer_element(self, position, valeur):
        assert position <= self.longueur(), "LA POSITION EST TROP GRANDE !!!!"
        if position == 0:
            self.ajouter_element_tete(valeur)
        else:
            temp = 1
            maillon = self.tete
            while temp < position:
                maillon = maillon.suivant
                temp += 1
            maillon.suivant = Maillon(valeur, maillon.suivant)

    def supprimer_element(self, position):
        assert not self.est_vide(), "LA LISTE EST VIDE !!!!!!!!!!!!!!!"
        assert position < self.longueur(), "LA POSITION EST TROP GRANDE !!!!"
        if position == 0:
            self.supprimer_element_tete()
        else:
            temp = 1
            maillon = self.tete
            while temp < position:
                maillon = maillon.suivant
                temp += 1
            maillon.suivant = maillon.suivant.suivant

    def chercher_element(self, valeur):
        temp = 0
        maillon = self.tete
        while maillon is not None and maillon.valeur != valeur:
            maillon = maillon.suivant
            temp += 1
        return temp if maillon is not None else -1

    def renverser(self):
        prev = None
        current = self.tete
        while current is not None:
            suivant = current.suivant
            current.suivant = prev
            prev = current
            current = suivant
        self.tete = prev

    def permuter_elements(self, position_1, position_2):
        assert 0 <= position_1 < self.longueur() and 0 <= position_2 < self.longueur(), "POSITION INCORRECTE !!!"
        if position_1 != position_2:
            temp = 0
            maillon_1, maillon_2 = None, None
            current = self.tete
            while temp <= position_2:
                if temp == position_1:
                    maillon_1 = current
                if temp == position_2:
                    maillon_2 = current
                current = current.suivant
                temp += 1
            maillon_1.valeur, maillon_2.valeur = maillon_2.valeur, maillon_1.valeur


# Example usage
l1 = Liste_chainee()
print(l1.est_vide())
l1.ajouter_element_queue(5)
l1.ajouter_element_queue(7)
l1.ajouter_element_queue(10)
l1.ajouter_element_queue(1)
print(l1.list())
print(l1.longueur())
l1.ajouter_element_tete(6)
print(l1.list())
l1.inserer_element(3, 8)
print(l1.list())
l1.supprimer_element(2)
print(l1.list())
print(l1.chercher_element(7))
l1.renverser()
print(l1.list())
l1.permuter_elements(1, 3)
print(l1.list())

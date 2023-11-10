class Maillon():
    def __init__(self, valeur = None, suivant = None):
        self.valeur = valeur
        self.suivant = suivant

class Liste_chainee():
    def __init__(self, tete = None):
        self.tete = tete
        
    def est_vide(self):
        if self.tete == None:
            return True
        else:
            return None
        
    def ajouter_element_queue(self, valeur):
        self.tete = Maillon(valeur)
        
        
m1 = Liste_chainee()
print(m1.est_vide())
m1.ajouter_element_queue(5)

        

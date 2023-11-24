import module_liste_chainee as m

class Pile():
    def __init__(self):
        self.valeurs = m.Liste_chainee()
        
    def est_vide(self):
        return self.valeurs.est_vide()
    
    def empiler(self, valeur):
        return self.valeurs.ajouter_element_queue(valeur)
    
    def depiler(self):
        dvaleur = self.valeurs.extrait_element(self.valeurs.longueur() - 1)
        a = self.valeurs.supprimer_element_queue()
        return print(dvaleur)
    
    def sommet(self):
        return print(self.valeurs.extrait_element(self.valeurs.longueur() - 1))
    
    def longeur(self):
        return print(self.valeurs.longueur())
    
    def tupl_e(self):
        return print(self.valeurs.list())

def main():
    pass         
        
if __name__ == "__main__":
    main()




import module_liste_chainee as m

class Pile():
    def __init__(self):
        self.valeurs = m.Liste_chainee()
        
    def est_vide(self):
        return self.valeurs.est_vide()
    
    def enfiler(self, valeur):
        return self.valeurs.ajouter_element_queue(valeur)
    
    def defiler(self):
        dvaleur = self.valeurs.extrait_element(self.valeurs.longueur() - 1)
        a = self.valeurs.supprimer_element_tete()
        return print(dvaleur)

    def longeur(self):
        return print(self.valeurs.longueur())
    
    def tupl_e(self):
        return print(self.valeurs.list())

def main():
    pass         

if __name__ == "__main__":
    main()
    
    
p1 = Pile()
p1.enfiler(18313)
p1.enfiler(68434)
p1.enfiler(46418)
p1.tupl_e()
p1.defiler()
p1.longeur()
p1.tupl_e()





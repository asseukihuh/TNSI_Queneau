class Maillon():
    def __init__(self, valeur = None, suivant = None):
        self.valeur = valeur
        self.suivant = suivant

class Liste_chainee():
    def __init__(self):
        self.tete = None
        
    def est_vide(self):
        return self.tete == None
        
    def ajouter_element_queue(self, valeur):
        if self.est_vide():
            self.tete = Maillon(valeur)
        else:
            maillon = self.tete
            while maillon.suivant != None:
                maillon = maillon.suivant
            maillon.suivant = Maillon(valeur)
    
    def list(self):
        a = []
        if self.est_vide():
            return a
        else:
            maillon = self.tete
            a.append(maillon.valeur)
            while maillon.suivant != None:
                maillon = maillon.suivant
                a.append(maillon.valeur)
        return a
    
    def longeur(self):
        if self.est_vide():
            return 0
        else:
            temp = 1
            maillon = self.tete
            while maillon.suivant != None:
                maillon = maillon.suivant
                temp += 1
        return temp
    
    def extrait_element(self, position):
        assert self.est_vide() == False, "LA LISTE EST VIDE !!!!!!!!!!!!!!!"
        assert position <= self.longeur(), "LA VALEUR EST TROP GRANDE !!!!"
        if self.longeur() > 1:
            temp = 1
            maillon = self.tete
            while maillon.suivant != None and temp != position:
                maillon = maillon.suivant
                temp += 1
        return maillon.valeur
    
    def ajouter_element_tete(self, valeur):
        self.tete = Maillon(valeur, self.tete)
        
    def supprimer_element_queue(self):
        maillon = self.tete
        i = 0
        position = self.longeur() - 2
        
        while i != position:
                maillon = maillon.suivant
                i = i + 1
        maillon.suivant = None
        
    def supprimer_element_tete(self):
        self.tete = self.tete.suivant
            
    def inserer_element(self, position, valeur):
        temp = 1
        maillon = self.tete
        while temp != position:
            maillon = maillon.suivant
            temp += 1
            #print(temp)
        self.suivant = Maillon(valeur)
        
        
        
    
    
    
          
l1 = Liste_chainee()
print(l1.est_vide())
l1.ajouter_element_queue(5)
print(l1.est_vide())
print(l1.tete.suivant)
l1.ajouter_element_queue(7)
l1.ajouter_element_queue(10)
l1.ajouter_element_queue(1)
print(l1.list())
print(l1.longeur())
print(l1.ajouter_element_tete(6))
print(l1.list())
print(l1.inserer_element(3, 8))
print(l1.list())





        

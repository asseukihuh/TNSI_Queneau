#Importation des modules
import tkinter

#Déclatation des Fonctions et des classes

class TipTop():
    def __init__(self, utilisateurs = []):
        self.utilisateurs = utilisateurs
        
    def max_like(self):
        a = len(self.utilisateurs)
        v = self.utilisateurs
        m = v[1]
        for i in range(a):
            if v[1].like < m.like:
                m = v[1]
            else :
                m = m
        print(m.nom)
            
        
        
        
        

class Utilisateur():
    def __init__(self, nom = '', like = 0, publications = 0):
        self.nom = nom
        self.like = like
        self.publications = publications
        
    def afficher_informations(self):
        print(self.nom,'a',self.like,'likes, sur', self.publications,'publications')
        
        
        
#Programme Principal
        
ut1 = Utilisateur('Timothée', 561, 5)
ut2 = Utilisateur('Timothée2', 953, 14)
ut3 = Utilisateur('Timothée3', 865, 9)
a = TipTop([ut1, ut2, ut3])
a.max_like()
ut1.afficher_informations()





        
## Importation des modules


## Déclaration des classes

class Fleur:
    couleurs_disponibles = ['blanc', 'rouge', 'jaune', 'bleu', 'rose', 'violet']
    
    def __init__(self, couleur='blanc', taille = 30, nbr_petales = 10, nbr_feuilles = 0):
        self.couleur = couleur
        self.taille = taille
        self.nbr_petales = nbr_petales
        self.nbr_feuilles = nbr_feuilles
        self.affiche_caracteristiques()
    
    #affichage variable
    def affiche_caracteristiques(self):
        print(f"Couleur: {self.couleur},",
        f"Taille: {self.taille},",
        f"Nombres petales: {self.nbr_petales},",
        f"Nombres feuilles: {self.nbr_feuilles}")
    
    #calcul variable
    def ajoute_petale(self):
        self.nbr_petales += 1
    
    #calcul variable
    def enleve_petale(self):
        self.nbr_petales -= 1
    
    #multiplication variable
    def allonge(self, x):
        assert x >= 0, "le paramètre doit être positif ou nul"
    
    #multiplication variable
    def pousse(self):
        self.taille *= 1.10
    
    #multiplication variable
    def est_fanee(self):
        if self.nbr_petales == 0:
            return True
        else:
            return False
        

## Déclaration des fonctions


## Programme principal
        
fleur_1 = Fleur()
fleur_2 = Fleur()
fleur_3 = Fleur()

fleur_2.couleur = 'rouge'
fleur_2.nbr_petales = 8
fleur_2.nbr_feuilles = 4
fleur_2.taille = 25

fleur_3.couleur = 'jaune'
fleur_3.nbr_petales = 16
fleur_3.nbr_feuilles = 8
fleur_3.taille = 12

bouquet = [fleur_1, fleur_2, fleur_3]

for i in range(len(bouquet)):
    print('Fleur n°', i + 1)
    bouquet[i].affiche_caracteristiques()
    print()    

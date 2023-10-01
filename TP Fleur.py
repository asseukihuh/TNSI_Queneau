class Fleur:
    couleurs_disponibles = ['blanc', 'rouge', 'jaune', 'bleu', 'rose', 'violet']
    
    def __init__(self, couleur='blanc', taille=20, nbr_petales=10, nbr_feuilles=0):
        self.couleur = couleur
        self.taille = taille
        self.nbr_petales = nbr_petales
        self.nbr_feuilles = nbr_feuilles
    
    def affiche_caracteristiques(self):
        print(f"Couleur: {self.couleur}, Taille: {self.taille} cm, Pétales: {self.nbr_petales}, Feuilles: {self.nbr_feuilles}")
    
    def ajoute_petale(self):
        self.nbr_petales += 1
    
    def enleve_petale(self):
        if self.nbr_petales > 0:
            self.nbr_petales -= 1
    
    def allonge(self, x):
        if x >= 0:
            self.taille += x
        else:
            print("Le paramètre doit être positif ou nul.")
    
    def pousse(self):
        self.taille *= 1.1
    
    def est_fanee(self):
        return self.nbr_petales == 0
    
    def couleurs_fleur(self):
        couleurs = {couleur: getattr(self, 'couleur').count(couleur) for couleur in self.couleurs_disponibles}
        total_apparitions = sum(couleurs.values())
        taux_apparition = {couleur: count/total_apparitions for couleur, count in couleurs.items()}
        return taux_apparition

    def croisement(self, autre_fleur):
        couleurs = [self.couleur, autre_fleur.couleur]
        taille = (self.taille + autre_fleur.taille) / 2
        nbr_petales = (self.nbr_petales + autre_fleur.nbr_petales) // 2
        nbr_feuilles = (self.nbr_feuilles + autre_fleur.nbr_feuilles) // 2
        return Fleur(couleurs, taille, nbr_petales, nbr_feuilles)


class Laboratoire_genetique:
    def croisement(self, fleur1, fleur2):
        couleurs = fleur1.couleurs + fleur2.couleurs
        taille = (fleur1.taille + fleur2.taille) / 2
        nbr_petales = (fleur1.nbr_petales + fleur2.nbr_petales) // 2
        nbr_feuilles = (fleur1.nbr_feuilles + fleur2.nbr_feuilles) // 2
        return Fleur(couleurs, taille, nbr_petales, nbr_feuilles)

    def croisement_bouquet(self, fleurs):
        nouveaux = []
        for i, fleur1 in enumerate(fleurs):
            for fleur2 in fleurs[i+1:]:
                nouveaux.append(self.croisement(fleur1, fleur2))
        return nouveaux + fleurs

    def croisement_bouquet_generation(self, fleurs, n):
        for _ in range(n):
            fleurs = self.croisement_bouquet(fleurs)
        return fleurs


fleur = Fleur()
fleur.affiche_caracteristiques()

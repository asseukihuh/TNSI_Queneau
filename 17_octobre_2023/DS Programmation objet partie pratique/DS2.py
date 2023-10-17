#Importation des modules

#Déclaration des fonctions

class Aliment:
    def __init__(self, e, p, g, l):
        self.energie = e
        self.proteines = p
        self.glucides = g
        self.lipides = l
        
    def get_energie(self):
        return self.energie
    
    def set_energie(self, n):
        self.energie = n
        
    def energie_reelle(self, masse):
        return masse*self.energie/100
        
        
#Programme Principal
    
farine_de_ble = Aliment(343,11.7,69.3,0.8)
lait = Aliment(65.1,3.32,4.85,3.63)
print(farine_de_ble.glucides)
farine_de_ble.proteines = 13.8
print(farine_de_ble.proteines)
farine_de_ble.set_energie(999)
print(farine_de_ble.get_energie())
print(lait.energie_reelle(245))

class Maillon():
    def __init__(self, valeur = None, suivant = None):
        self.valeur = valeur
        self.suivant = suivant
        
m1 = Maillon(5)
m2 = Maillon(7)

print(id(m1),hex(id(m1)),bin(id(m1)))

print(id(m2),hex(id(m2)),bin(id(m2)))

print(m1.valeur)
print(m2.valeur)

m2.valeur = 9
print(m2.valeur)

m3 = Maillon(2)
m4 = Maillon(11)

l1 = m1
l1.suivant = m2
print(l1.suivant.valeur)
l1.suivant.suivant = m3
l1.suivant.suivant.suivant = m4
print(l1.suivant.suivant.valeur, l1.suivant.suivant.suivant.valeur)

l2 = Maillon(1, Maillon(2, Maillon(3, Maillon(4))))
print(l2.valeur, l2.suivant.valeur, l2.suivant.suivant.valeur, l2.suivant.suivant.suivant.valeur, l2.suivant.suivant.suivant.suivant)






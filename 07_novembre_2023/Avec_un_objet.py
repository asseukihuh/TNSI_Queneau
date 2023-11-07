class Maillon():
    def __init__(self, valeur = None, suivant = None):
        self.valeur = valeur
        self.suivant = suivant
        
a = Maillon(5)
b = Maillon(7)

print(id(a),hex(id(a)),bin(id(a)))

print(id(b),hex(id(b)),bin(id(b)))

c = a.valeur
print(c)
d = b.valeur
print(d)

b.valeur = 9
print(b.valeur)

l1 = a
#l1 = [a.valeur, None]
print(l1)

l1 = 
#l1[1] = [b.valeur, None]
print(l1)

e = Maillon(2)
f = Maillon(11)
l1[1][1] = [e.valeur, None]
l1[1][1][1] = [f.valeur, None]
print(l1)






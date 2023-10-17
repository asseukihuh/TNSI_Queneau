#Importation des modules

#Déclaration des fonctions

class AdresseIP:
    
    def __init__(self, adresse):
        self.adresse = adresse
        
    def liste_octet(self):
        """revoie une liste de nombres entiers, la liste des octets de
        l'adresse IP"""
        return [int(i) for i in self.adresse.split(".")]
    
    def est_reservee(self):
        """renvoie True si l'adresse IP est une adresse reservée,
        False sinon"""
        return True or False
    
    def adresse_suivante(self):
        """revoie un objet de AdresseIp avec l'adresse IP qui suit
        l'adresse self si elle existe et False sinon"""
        a = self.liste_octet()
        if a[3] < 254:
            octet_nouveau = a[3] + 1
            return AdresseIP('192.168.0.'+ str(octet_nouveau))
        else:
            return False
        
    def plus_grand(self, adresse1):
        a = self.liste_octet()
        if a[0] > adresse1[0]:
            return(a)
        elif a[0] < adresse1[0]:
            return(adresse1)
        elif a[1] > adresse1[1]:
            return(a)
        elif a[1] < adresse1[1]:
            return(adresse1)
        elif a[2] > adresse1[2]:
            return(a)
        elif a[2] < adresse1[2]:
            return(adresse1)
        elif a[3] > adresse1[3]:
            return(a)
        elif a[3] < adresse1[3]:
            return(adresse1)
        else:
            return None  

#Programme Principal

adresse1 = AdresseIP('192.168.0.1')
adresse2 = AdresseIP('192.168.0.2')
adresse3 = AdresseIP('192.168.0.3')
adresse4 = AdresseIP('192.168.0.2')
adresse5 = AdresseIP('192.168.0.0')
adresse6 = AdresseIP('192.168.0.2')
adresse7 = AdresseIP('192.212.0.2')


print(adresse1.est_reservee())
print(adresse3.est_reservee())
print(adresse3.adresse_suivante().adresse)
d = adresse5.liste_octet()
e = adresse7.liste_octet()
print(adresse4.plus_grand(d))
print(adresse6.plus_grand(e))


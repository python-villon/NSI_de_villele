import random

class Chien:

    def __init__(self, nom, aboiement, sante):
        self.nom = nom
        self.aboiement = aboiement
        self.sante = sante

    def machouiller(self, S):
        L = ''.join(random.sample(S,len(S)))
        return L

    def aboyer(self):
        return ('Grr...'+self.aboiement)

    def mordre(self, chien):
        if chien.sante > 0:
            chien.sante -= 1

    def manger(self):
        if self.sante < 10:
            self.sante += 1

    

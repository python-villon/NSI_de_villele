from vizu_arbreb import VizuArbreB

class Noeud:
    '''
    Classe implémentant un noeud d'arbre binaire étiqueté disposant de 3 attributs :
    - valeur : la valeur de l'étiquette,
    - gauche : None si le sous-arbre gauche est vide, sinon le noeud racine du sous-arbre gauche.
    - droit : None si le sous-arbre droit est vide, sinon le noeud racine du sous-arbre droit.
    
    '''
    def __init__(self, v, g, d):
        self.valeur = v
        self.gauche = g
        self.droit = d
        
def taille(arbre):
    '''Renvoie la taille d'un arbre binaire.'''
    if arbre == None : 
        return 0
    else :
        t = 1 + taille(arbre.gauche) + taille(arbre.droit)
        return t
    
def hauteur(arbre):
    '''Renvoie la hauteur d'un arbre binaire (racine de hauteur 1)'''
    if arbre == None : 
        return 0
    else :
        h = 1 + max(hauteur(arbre.gauche), hauteur(arbre.droit))
        return h

def copie(arbre):
    '''Renvoie une copie d'un arbre binaire.'''
    if arbre == None : 
        return None
    else :
        c = Noeud(arbre.valeur, copie(arbre.gauche), copie(arbre.droit))
        return c

def schema(arbre):
    '''Affiche une représentation visuelle de l'arbre binaire (requiert graphviz).'''
    VizuArbreB(arbre)
    
def arbre_parfait(k):
    '''
    Renvoie un arbre parfait de hauteur k dont les sommets sont étiquetés de 1 à (2^k)-1 
    en étiquetant niveau après niveau, de gauche à droite (en largeur).
    '''
    def ap(k, v):
        if k == 0:
            return None
        else:
            return Noeud(v, ap(k-1, 2*v), ap(k-1, 2*v + 1))
    return ap(k, 1)

def somme(arbre):
    '''Renvoie la somme des valeurs d'un arbre binaires dont les étiquettes sont des nombres.'''
    if arbre == None : 
        return 0
    else :
        s = arbre.valeur + somme(arbre.gauche) + somme(arbre.droit)
        return s

def maximum(arbre):
    '''Renvoie la valeur maximale d'un arbre binaire dont les étiquettes sont des nombres.'''
    if arbre == None : 
        return 0
    else :
        m = max(arbre.valeur, maximum(arbre.gauche), maximum(arbre.droit))
        return m
    
def minimum(arbre):
    '''Renvoie la valeur minimale d'un arbre binaire dont les étiquettes sont des nombres.'''
    if arbre == None : 
        return 0
    else :
        m = min(arbre.valeur, minimum(arbre.gauche), minimum(arbre.droit))
        return m
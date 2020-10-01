class Noeud:
    def __init__(self, etiquette, sag, sad):
        assert type(sag) == ArbreBR and type(sad) == ArbreBR       
        self.etiquette = etiquette
        self.sag = sag
        self.sad = sad
        
    def get_etiquette(self):
        return self.etiquette
    
    def get_gauche(self):
        return self.sag
    
    def get_droite(self):
        return self.sad

    def change_etiquette(self, etiquette):
        return Noeud(etiquette, self.get_gauche(), self.get_droite())

    def change_gauche(self, arbre):
        return Noeud(self.get_etiquette(), arbre, self.get_droite())
    
    def change_droite(self, arbre):
        return Noeud(self.get_etiquette(), self.get_gauche(), arbre)
    
class ArbreBR:
    def __init__(self, *etiquette_et_sous_arbres):
        args = etiquette_et_sous_arbres
        assert len(args) in (0, 3), 'Pour un arbre non vide, fournir une étiquette et deux sous-arbres'
        if len(args) == 0:
            self.noeud = None
            self.hauteur = 0
        else:
            gauche = args[1]
            droite = args[2]
            self.noeud = Noeud(args[0], gauche, droite)
            self.hauteur = 1 + max(gauche.get_hauteur(), droite.get_hauteur())
        
    
    ########################################################################
    #  METHODES POUR QUE LE REEQUILIBRAGE SOIT EN COMPLEXITE CORRECTE
    #  (on pourrait s'en dispenser)
    ########################################################################
    
    def get_hauteur(self):
        return self.hauteur
    
    def change_hauteur(self, hauteur):
        a = ArbreBR(self.get_etiquette(), self.get_gauche(), self.get_droite())
        a.hauteur = hauteur                                                      #<---- !
        return a
    
    ########################################################################
    #  FIN DES METHODES POUR LE REEQUILIBRAGE 
    ########################################################################
    
    
    def est_vide(self):
        return self.noeud is None
    
    def est_feuille(self):
        return not self.est_vide() and self.get_gauche().est_vide() and self.droite().est_vide()
            
    def get_etiquette(self):
        assert not self.est_vide()
        return self.noeud.get_etiquette()
    
    def get_gauche(self):
        assert not self.est_vide()
        return self.noeud.get_gauche()
    
    def get_droite(self):
        assert not self.est_vide()
        return self.noeud.get_droite()
        
    def change_etiquette(self, etiquette):
        assert not self.est_vide()
        return ArbreBR(etiquette, self.get_gauche(), self.get_droite())
        
    def change_gauche(self, arbre):
        assert not self.est_vide()
        return ArbreBR(self.get_etiquette(), arbre, self.get_droite())
    
    def change_droite(self, arbre):
        assert not self.est_vide()
        return ArbreBR(self.get_etiquette(), self.get_gauche(), arbre)       
    
    
def hauteur(arbre):
    '''
    Renvoie la hauteur de l'arbre
    '''
    if arbre.est_vide():
        return 0
    else: 
        return 1 + max(hauteur(arbre.get_droite()) , hauteur(arbre.get_gauche()))
    
def taille(arbre):
    '''
    Renvoie la taille de l'arbre
    '''
    if arbre.est_vide():
        return 0
    else: 
        return 1 + taille(arbre.get_droite()) + taille(arbre.get_gauche())
    
def minimum(arbre):
    '''
    Renvoie la plus petite étiquette présente dans l'arbre
    '''
    assert not arbre.est_vide()
    if arbre.get_gauche().est_vide():
        return arbre.get_etiquette()
    else:
        return minimum(arbre.get_gauche())

def maximum(arbre):
    '''
    Renvoie la plus grande étiquette présente dans l'arbre
    '''
    assert not arbre.est_vide()
    if arbre.get_droite().est_vide():
        return arbre.get_etiquette()
    else:
        return maximum(arbre.get_droite())

def rechercher(clef, arbre): #possible en while
    '''
    Renvoie True ou False selon que la clef est présente ou pas dans l'arbre
    '''
    if not arbre.est_vide():
        if arbre.get_etiquette() > clef:
            return recherche(clef, arbre.get_gauche())
        elif arbre.get_etiquette() < clef:
            return recherche(clef, arbre.get_droite())
        else:
            return True
    return False     
            
def inserer(clef, arbre):
    '''
    Renvoie un nouvel arbre binaire de recherche correspondant 
    à arbre dans lequel on a inséré clef
    '''
    if arbre.est_vide():
        a = ArbreBR(clef, ArbreBR(), ArbreBR())
    elif arbre.get_etiquette() > clef:
        a = arbre.change_gauche(inserer(clef, arbre.get_gauche()))
    elif arbre.get_etiquette() < clef:
        a = arbre.change_droite(inserer(clef, arbre.get_droite()))
    elif arbre.get_etiquette() == clef:
        a = arbre
    a = _reequilibrer(a)                        
    return a

def supprimer(clef, arbre):
    '''
    Renvoie un nouvel arbre binaire de recherche correspondant 
    à arbre duquel on a supprimé clef
    '''    
    if arbre.est_vide():
        a = ArbreBR()
    elif arbre.get_etiquette() > clef:
        a = arbre.change_gauche(supprimer(clef, arbre.get_gauche()))
    elif arbre.get_etiquette() < clef:
        a = arbre.change_droite(supprimer(clef, arbre.get_droite()))
    elif arbre.get_etiquette() == clef:
        if arbre.get_droite().est_vide():
            a = arbre.get_gauche()
        else:
            a = arbre.change_etiquette(minimum(arbre.get_droite()))
            d = _supprimer_min(a.get_droite())
            a = a.change_droite(d)
    a = _reequilibrer(a)                        
    return a



def _supprimer_min(arbre):
    if arbre.get_gauche().est_vide():
        a = arbre.get_droite()
    else:
        a = arbre.change_gauche(_supprimer_min(arbre.get_gauche()))
    a = _reequilibrer(a)                        
    return a
        
def _supprimer_max(arbre):
    if arbre.get_droite().est_vide():
        a = arbre.get_gauche()
    else:
        a = arbre.change_droite(_supprimer_max(arbre.get_droite()))
    a = _reequilibrer(a)                        
    return a

def _reevaluer_hauteur(arbre):
    if not arbre.est_vide():
        return 1 + max(arbre.get_gauche().get_hauteur(), arbre.get_droite().get_hauteur())
    else:
        return 0
    
    
def _rotation_droite(arbre):
    assert not arbre.est_vide() and not arbre.get_gauche().est_vide()
    gauche = arbre.get_gauche()
    arbre_a = arbre.change_gauche(gauche.get_droite())
    arbre_a = arbre_a.change_hauteur(_reevaluer_hauteur(arbre_a))
    gauche = gauche.change_droite(arbre_a)
    gauche = gauche.change_hauteur(_reevaluer_hauteur(gauche))
    return gauche
    
def _rotation_gauche(arbre):
    assert not arbre.est_vide() and not arbre.get_droite().est_vide()
    droite = arbre.get_droite()
    arbre_a = arbre.change_droite(droite.get_gauche())
    arbre_a = arbre_a.change_hauteur(_reevaluer_hauteur(arbre_a))
    droite = droite.change_gauche(arbre_a)
    droite = droite.change_hauteur(_reevaluer_hauteur(droite))
    return droite
    
def _reequilibrer(arbre):
    if arbre.est_vide():
        return ArbreBR()
    hg = arbre.get_gauche().get_hauteur()
    hd = arbre.get_droite().get_hauteur()
    if hg > hd + 1:
        hgg = arbre.get_gauche().get_gauche().get_hauteur()
        hgd = arbre.get_gauche().get_droite().get_hauteur()
        if hgg >= hgd:
            a = _rotation_droite(arbre)
        else:
            a = arbre.change_gauche(_rotation_gauche(arbre.get_gauche()))
            a = _rotation_droite(a)
    elif hd > hg + 1:
        hdd = arbre.get_droite().get_droite().get_hauteur()
        hdg = arbre.get_droite().get_gauche().get_hauteur()
        if hdd >= hdg:
            a = _rotation_gauche(arbre)
        else:
            a = arbre.change_droite(_rotation_droite(arbre.get_droite()))
            a = _rotation_gauche(a)
    else:
        a = arbre.change_hauteur(_reevaluer_hauteur(arbre))
    return a
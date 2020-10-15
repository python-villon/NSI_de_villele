class Cellule:
    
    def __init__(self, element, succ):
        self.element = element
        self.succ = succ
        
    def get_element(self):
        return self.element
    
    def get_succ(self):
        return self.succ

    def set_succ(self, cell):
        self.succ = cell
        
    def __repr__(self):
        return '|' + str(self.element)
    
class Pile:
    '''
    Implémente une SDD de pile.
    >>> p = Pile()
    >>> p.ajouter(4)
    >>> p.ajouter(7)
    >>> p.ajouter(13)
    >>> p.ajouter(65)
    >>> x = p.extraire()   # x = 65 et 65 a été retiré de la file
    '''
    
    def __init__(self):
        self.cellule = None
        
    def est_vide(self):
        '''Renvoie True si la pile est vide, False sinon.'''
        return self.cellule == None
        
    def ajouter(self, element):
        '''Mute la pile pour lui ajouter element au sommet.'''
        self.cellule = Cellule(element, self.cellule)
    
    def extraire(self):
        '''Mute la pile pour en retirer et renvoyer l'élément au sommet.'''
        assert not self.est_vide()
        x = self.cellule.get_element()
        self.cellule = self.cellule.get_succ()
        return x
        
    def __repr__(self):
        '''Pour la représentation textuelle de la pile via print().''' 
        c = self.cellule
        s = '|'
        while not c is None:
            s = c.__repr__() + s
            c = c.get_succ()
        return s[:]  + '\u2B80'  

class File:
    '''
    Implémente une SDD de file.
    >>> f = File()
    >>> f.ajouter(4)
    >>> f.ajouter(7)
    >>> f.ajouter(13)
    >>> f.ajouter(65)
    >>> x = f.extraire()   # x = 4 et 4 a été retiré de la file
    '''
    
    def __init__(self):
        self.tete = None
        self.dernier = None
        
    def est_vide(self):
        '''Renvoie True si la file est vide, False sinon.'''
        return self.tete == None
        
    def ajouter(self, element):
        '''Mute la file pour lui ajouter element en queue de file.'''
        if not self.est_vide():
            self.dernier.set_succ(Cellule(element, None))
            self.dernier = self.dernier.get_succ()
        else:
            self.dernier = Cellule(element, None)
            self.tete = self.dernier
    
    def extraire(self):
        '''Mute la file pour en retirer et renvoyer l'élément situé en tête de file.'''
        assert not self.est_vide()
        x = self.tete.get_element()
        self.tete = self.tete.get_succ()
        return x 
        
    def __repr__(self):
        '''Pour la représentation textuelle de la file via print().''' 
        c = self.tete
        s = ''
        while not c is None:
            s = s + c.__repr__()
            c = c.get_succ()
        return '\u2BA4' + s[:] + '\u2BA0'   
                  
class Liste:
    '''
    Implémente une SDD de Liste.
    >>> l = Liste()
    >>> l.ajouter(4)
    >>> l.ajouter(7)
    >>> l.ajouter(13)
    >>> l.ajouter(65)
    >>> x = l.extraire()   #x = 65, 65 a été retiré de la liste, l contient donc 4, 7 et 13
    >>> x = l.queue().tete() #x = 7, 7 n'a pas été retiré de la liste, l contient donc 4, 7 et 13
    '''
    
    def __init__(self):
        self.cellule = None
        
    def est_vide(self):
        '''Renvoie True si la liste est vide, False sinon.'''
        return self.cellule == None
    
    def ajouter(self, element):
        '''Mute la liste pour lui ajouter element au sommet.'''
        if not self.est_vide():
            copie = Liste()
            copie.cellule = self.cellule
            self.cellule = Cellule(element, copie)
        else:
            self.cellule = Cellule(element, Liste())
        
    def extraire(self):
        '''Mute la liste pour en retirer et renvoyer l'élément situé en tête de liste.'''
        assert not self.est_vide()
        x = self.cellule.get_element()
        self.cellule = self.cellule.get_succ()
        return x
    
    def queue(self):
        '''Renvoie la liste constituant la queue de la liste.'''
        assert not self.est_vide()
        return self.cellule.get_succ()
    
    def tete(self):
        '''Renvoie l'élément situé en tête de liste sans l'extraire de la liste.'''
        assert not self.est_vide()
        return self.cellule.get_element()
    
    def __repr__(self):
        '''Pour la représentation textuelle de la pile via print().'''
        c = self
        s = ''
        while not c.est_vide():
            s = c.tete().__repr__() + '|' + s
            c = c.queue()
        return s[:]  + '\u2B80'
    
    
    
    
    
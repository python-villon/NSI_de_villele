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
    
    def __init__(self):
        self.cellule = None
        
    def est_vide(self):
        return self.cellule == None
        
    def empiler(self, element):
        self.cellule = Cellule(element, self.cellule)
    
    def depiler(self):
        assert not self.est_vide()
        x = self.cellule.get_element()
        self.cellule = self.cellule.get_succ()
        return x
        
    def __repr__(self):
        c = self.cellule
        s = '|'
        while not c is None:
            s = c.__repr__() + s
            c = c.get_succ()
        return s[:]  

                  

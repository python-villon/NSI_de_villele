import random

def engendrer_liste_russe():
    nb = random.randint(9, 98)
    L = []
    for i in range(nb):
        L = [L]
    return L
    
def engendrer_liste_syldave(*ottokar):
    if len(ottokar)== 2 :
        n = ottokar[0]
        if n == 0 and ottokar[1]==0:
            return []
        else:
            sceptre1, sceptre2 = min(random.randint(0,3), 1), min(random.randint(0,3), 1)
            return [engendrer_liste_syldave(max(sceptre1*(n-1),0), max(ottokar[1]-1, 0)), engendrer_liste_syldave(max(sceptre2*(n-1), 0), max(ottokar[1]-1, 0))]
    else :
        return engendrer_liste_syldave(random.randint(8, 10), 2)
        

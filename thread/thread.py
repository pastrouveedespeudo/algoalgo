import threading

from CONFIG import PONCTUATION


#un truk qui écrit du code


GLOBAL = []

def entree():

    print('cherche moi un restaurant pres de chez moi')
    print('fait moi un dessin')
    print('qui a fais la joconde ?')
    print('envoie un mail')
    print('qui est le plus beau ?')
    print("quel temps fait il aujourdh'ui?")
    print("que veut dire le mot 'pierre' ?")
    print("fais moi programme qui fait une table de mulitplication")
    print("corrige moi ce code stp")
    print("corrige moi ce texte stp")

    print("quand c'est les marchés de crest ?")
    print("fais moi une analyse de l'image, trouves tu 5 balles par terre ? utilise le satellite, direction crest stp")
    
    print("")
    oInput = input('Que veux tu faire ?')
    
    return oInput




def traitement_entree():
    """on split chaque mot"""

    entrance = entree()
    entrance = entrance.split()
    
    for i in entrance:
        GLOBAL.append(i.lower())
        


def connaissance():
    """connais ton la phrase ? si oui reponse
    sinon analyse si reponse ajout database"""
    pass





def analyse_phrase():
    """une question un ordre ?"""

    liste = [j for i in GLOBAL for j in i for k in PONCTUATION if j == k]
    print(liste)
    return liste




def verbe():
    """Par les verbes on doit faire l'action"""

    pass


def mot_cle():
    """les noms communs et combien par exemple ?"""

    pass



th_entree = threading.Thread(target=traitement_entree)
th_entree.start()
th_entree.join()

th1 = threading.Thread(target=analyse_phrase)
th2 = threading.Thread(target=mot_cle)
th3 = threading.Thread(target=verbe)

th1.start()
th2.start()
th3.start()

th1.join()
th2.join()
th3.join()

print('SUITEEE')


def insertion_database():
    """On stock la phrase et ce qu'on a fait avec"""
    pass

























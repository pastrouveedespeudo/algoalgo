import threading
import requests
from bs4 import BeautifulSoup

#PARTIE PONCTUATION
from CONFIG import PONCTUATION
from CONFIG import PONCTUATION_ASSOCIATION
from CONFIG import PONCTUATION_OUT


#PARTIE VERBE
from CONFIG import PATH_VERBE
from CONFIG import PRONOM_PERSONNEL


from analyse_ponctuation_function import analyse_phrase





#NE surtout pas écrire les print faut des truks qui le fasse

#un truk qui écrit du code

#ca inclus de lui dire quels ont été les étapes
#ca inclus de lui dire en détail les choses
#ensuite y mettre le truk vocal


#image cnn
#traitement de la parole lstl


GLOBAL = []


def entree():


    print("qui a fait la joconde ? et le radeau de la méduse ?")
    print('qui a fais la joconde ?')
    print('qui est mona lisa ?')
    print('qui est le plus beau ?')
    print("est ce que je suis bete ?")
    print("quel temps fait il aujourdh'ui?")
    print("que veut dire le mot 'pierre' ?")
    print('de quelle couleur est un poussin ?')
    print("Y a til du vert dans l'image ?")
    print("pourquoi pleut il ?")
    print("quand c'est les marchés de crest ?")

    
    print("\n\n\n\n")

    print('cherche moi un restaurant pres de chez moi')
    print("trouve l'adresse du concervatoire.")
    print("ou est le concervatoire ?")
    print("trouve la dérivée de x^2")


    print('fait moi un dessin')
    print("fais moi un poeme")
    #prend toutes les phrases on fait moyenne des phrases mot
    #on ressort lagencement
    

    print('envoie un mail')
    
    print("que veut dire en francais le mot stone")

    print("fais moi programme qui fait une table de mulitplication")
    print("corrige moi ce code stp")
    print("corrige moi ce texte stp")
    

    
    print("rajoute l'heure qu'il est dans la table de multiplication")
    print("qu'est ce qui différencie un chat d'un chien ?")

    
    print("résume moi ce texte")
    print("créer moi un environement virtuel, et un site sous django")
    print("le nombre de bouchons a crest")

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
        




def analyse_ponctuation():
    """une question un ordre ?"""
    #ICI   Il va falloir savoir si continuité ou pas genre les virgules

    liste = analyse_phrase(GLOBAL, PONCTUATION)
    
    for i in liste:

        for j in i:
            for key, value in PONCTUATION_ASSOCIATION.items():
                if j == key:
                    i.append([value])

    return liste
    #PREMIERE LISTE ICI   




def verbe():
    """Par les verbes on doit faire l'action"""

    liste_verbe = []

    for mot in GLOBAL:

        path = PATH_VERBE.format(mot)
        request_html = requests.get(path)
        page = request_html.content
        soup_html = BeautifulSoup(page, "html.parser")
        propriete = soup_html.find_all("td")

        for i in propriete:
            for pronom in PRONOM_PERSONNEL:
                recherche = str(i).find(str(pronom))
                
                if recherche >= 0:
                    liste_verbe.append([mot, pronom])
                    #on cherche je tu il nous vous ils


    return liste_verbe
    #DEUXIEME LISTE



def mot_cle():
    """les noms communs et combien par exemple ?"""
    #radeau de la méduse ?
    #mona lisa ?
    pass






th_entree = threading.Thread(target=traitement_entree)
th_entree.start()
th_entree.join()



#PREMIERE PARTIE
th1 = threading.Thread(target=analyse_ponctuation)
th2 = threading.Thread(target=mot_cle)
th3 = threading.Thread(target=verbe)

th1.start()
th2.start()
th3.start()

th1.join()
th2.join()
th3.join()



print('SUITEEE')



#DEUXIEME PARTIE

























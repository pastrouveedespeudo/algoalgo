from database import *
from traitement_nombre import *


class entree:
    def entree(self):
        Oinput = input('affiche 5 + 5')


        splitage = Oinput.split()
        
        sortie = []
        

        indexage = 0
        for i in splitage:

            try:
                i = int(i)
                if i == int(i):
                    print("oui", indexage)
                    sortie.append([i, indexage])
                    
            except:
                pass
            
            finally:
                indexage += 1

                
        print(sortie)
        
        for cle, valeur in dico.items():
            pass




if __name__ == "__main__":

    entree = entree()
    entree.entree()

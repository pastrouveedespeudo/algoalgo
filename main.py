import écriture
import importlib

from input import entree
from database import FONCTION
from database import AFFICHAGE_BOUCLE



#définir la fonction
#définir si y'a parametres
#faut il faire une boucle ?
#faut il afficher?
#que faut il afficher ? et ou?





#combien de fonction ?
#quoi return ?





class main:
    def entrance(self):
        #on fractionne l'entrée
        
        entrance = entree.entree(self)
        split = entree.split(self, entrance)
        return split

    def pré_traitement(self, entrance):
        #on récupere les print
        #ex: affiche la affiche
        #-> print() + 2 fois a la place 0 et 2
        self.entrance = entrance

        mot_clé = entree.recherche_mot_clé(self, self.entrance)

        return mot_clé


    def écriture_de_la_fonction(self):
        entree.écriture_fonction(self, FONCTION['debut'])
        entree.écriture_fonction(self, FONCTION['fin'])
        
    def écriture_corps_fonction(self, mot_clé):
        self.mot_clé = mot_clé

        multi = ""
        affichage = ''
        
        for i in self.mot_clé:
            for j in i:
                if j == 'affichage':
                    affichage = True
                if j == 'multiplication':
                    multi = True
                    index = self.mot_clé.index(i)
                    entree.écriture_ligne2(self, self.mot_clé[index][1][0])
                    entree.écriture(self, 10)
                    entree.écriture(self, self.mot_clé[index][1][1])
                    
                    if affichage == True:
                        entree.écriture_ligne3_indentation(self, AFFICHAGE_BOUCLE[0]['debut'])
                        entree.écriture(self, int(self.mot_clé[index][2][0]))
                        entree.écriture(self, AFFICHAGE_BOUCLE[0]['fin'])
                        entree.reload(self, écriture)


        
        for i in self.mot_clé:
            for j in i:
                if j == 'affichage' and multi == "":
                    entree.écriture_ligne2(self, self.mot_clé[0][1][0])
                    entree.écriture(self, self.mot_clé[0][3][1])
                    entree.écriture(self, self.mot_clé[0][1][1])
                    entree.reload(self, écriture)

if __name__ == "__main__":


    main = main()
    entrance = main.entrance()
    mot_clé = main.pré_traitement(entrance)
    main.écriture_de_la_fonction()
    main.écriture_corps_fonction(mot_clé)



    try:
        écriture.function()
    except:
        pass
    

    


















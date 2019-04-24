import importlib
import écriture
from database import AFFICHAGE, LISTE_AFFICHAGE



class entree:
    def entree(self):

        #affiche bonjour
        #affiche la table de 5
        #affiche 5 + 5
        Oinput = input('affiche bonjour')
        return Oinput

    def split(self, Oinput):
        splitage = Oinput.split()
        return splitage


    def recherche_mot_clé(self, para):

        liste = [i for i in LISTE_AFFICHAGE for j in para if i == j]
        if liste:
            dico = [valeur for cle, valeur in AFFICHAGE.items()]
            mot = "'" + para[1:][0] + "'"

            return dico, mot, False

    def nombre_para(self):
        return 1
 

    def fonction(self):
        corps_debut = 'def the_function('
        corps_fin = '):'

        return corps_debut, corps_fin
        

    def écriture_fonction(self, para):
        with open('écriture.py', 'a') as file:
            file.write(str(para))
        

    def écriture(self, para):
        with open('écriture.py', 'a') as file:
            file.write(str(para))
  
            
    def écriture_ligne2(self, para):
        with open('écriture.py', 'a') as file:
            file.write('\n')
            file.write('    ')
            file.write(para)


    def traitement(self, para):
        splitage = para.split()


        print(splitage)
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





    def parametrage(self, parametre, para_ou_non):

        if para_ou_non == False:
            return ""
        else:

            parametres = ''
            nom = 'para'
            compteur = 0
            for i in range(parametre):
                name = nom + str(compteur)
                
                parametres += name
                
                compteur += 1
                
            return parametres



    def reload(self, para):
        self.para = para
        importlib.reload(self.para)





##
##def the_function():
##
##    for i in range(10):
##        print(5*i)
##
##
##the_function()













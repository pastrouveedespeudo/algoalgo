import importlib
import écriture

from database import AFFICHAGE
from database import LISTE_AFFICHAGE

from database import LISTE_TABLE_MULITPLICATION
from database import TABLE_MULITPLICATION

from database import BOUCLE_FOR



class entree:
    def entree(self):

        #affiche bonjour
        #affiche la table de 5
        #affiche 5 + 5
        print('affiche la table de multiplication de 5')
        print('affiche moi la définition de cailloux')
        Oinput = input('affiche bonjour')
        return Oinput

    def split(self, Oinput):
        splitage = Oinput.split()
        return splitage


    def recherche_mot_clé(self, para):

        LA_LISTE = []

        affichage = [i for i in LISTE_AFFICHAGE for j in para if i == j]

        c = 0
        affichage2 = []
        for i in para:
            for j in affichage:
                if i == j:
                    affichage2.append(c)
                    break
            c+=1

        if affichage:
            dico = [valeur for cle, valeur in AFFICHAGE.items()]
            nb = len(affichage2)
            LA_LISTE.append(('affichage', dico, nb, para[affichage2[0]:],affichage2))

            
    
        mul = ' '.join(para)
        injonction = []
        
        for i in LISTE_TABLE_MULITPLICATION:
            find_mot = str(mul).find(str(i))
            
            if find_mot >= 0:
                
                nouveau_mul = mul[find_mot:int(find_mot) + int(len(i))]
                nouveau_mul = nouveau_mul.replace(' ','')
                mul2 = mul[:find_mot] + nouveau_mul + mul[int(find_mot) + int(len(i)):]
                       
                mul2 = mul2.split()
                index = mul2.index(nouveau_mul)

                integer = []
                for j in mul2:
                    try:
                        j = int(j)
                        if j == int(j):
                            integer.append(j)
                    except:
                        pass
                    

                LA_LISTE.append(('multiplication', TABLE_MULITPLICATION, integer, index))
    




        return LA_LISTE





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






##def the_function():
##
##    for i in range(10):
##        print(5*i)
##
##
##the_function()
##
##
##def the_function():
##    print('bonjour')











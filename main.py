from input import entree
import écriture

class main:
    def entrée(self):
        entrance = entree.entree(self)
        return entrance
    
    def split(self, entrance):
        return entree.split(self, entrance)

    def traitement_mot_clé(self, para):
        mot_cle = entree.recherche_mot_clé(self, para)
        return mot_cle
    
    def parametre(self):
        nb_para = entree.nombre_para(self)
        return nb_para

    def corps_fonction(self):
        corps = entree.fonction(self)
        return corps

    def écriture_fonction(self, para):
        entree.écriture_fonction(self, para)

    def écriture_l2(self, para):
        entree.écriture_ligne2(self, para)

    def écriture(self, para):
        entree.écriture(self, para)


    def parametrage(self, parametre):

        parametres = ''
        nom = 'para'
        compteur = 0
        for i in range(parametre):
            name = nom + str(compteur)
            
            parametres += name
            
            compteur += 1
            
        return parametres
        
    def reload(self, para):
        entree.reload(self, para)
    
if __name__ == "__main__":


    main = main()
    
    entrance = main.entrée()
    split = main.split(entrance)

    #noms de parametres
    c = main.parametre()
    parametres = main.parametrage(c)


    a = main.corps_fonction()
    b = main.traitement_mot_clé(split)


    main.écriture_fonction(a[0])
    main.écriture(parametres)
    main.écriture_fonction(a[1])

    main.écriture_l2(b[0][0])
    main.écriture(parametres)
    main.écriture(b[0][1])

    main.reload(écriture)
    écriture.the_function('bonjour')
    


    


















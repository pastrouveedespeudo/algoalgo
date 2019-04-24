from input import entree
import écriture





#définir la fonction
#définir si y'a parametres
#faut il faire une boucle ?
#faut il afficher?
#que faut il afficher ? et ou?





#combien de fonction ?
#quoi return ?





class main:
    def main(self):
        entrance = entree.entree(self)
        split = entree.split(self, entrance)
        print(split)

        
        #noms de parametres
        c = main.parametre()

        a = main.corps_fonction()
        b = main.traitement_mot_clé(split)
        parametres = main.parametrage(c, b[2])

        main.écriture_fonction(a[0])
        main.écriture(parametres)
        main.écriture_fonction(a[1])

        main.écriture_l2(b[0][0])
        main.écriture(parametres)
        main.écriture(b[1])
        main.écriture(b[0][1])

        main.reload(écriture)
        écriture.the_function() 

if __name__ == "__main__":


    main = main()
    main.main()

    


    


















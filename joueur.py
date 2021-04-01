from detective import *

class Joueur :


    def __init__(self):

        self.de=De()


    def jouer(self):

        x=self.de.lancer_de()

        if x==2:
            a=int(input("Voulez-vous avancer de 1 ou 2 cases ? Tapez '1' ou '2'"))
        while a>2 or a<=0:
            a=int(input("Voulez-vous avancer de 1 ou 2 cases ? Tapez '1' ou '2'"))
        joueur.avance(a)


        if x==3:
            a=int(input("Voulez-vous avancer de 1, 2 ou 3 cases ? Tapez '1' , '2' ou '3"))
        while a>3 or a<=0:
            a=int(input("Voulez-vous avancer de 1, 2 ou 3 cases ? Tapez '1' , '2' ou '3'"))
        joueur.avance(a)


        if x==4:
            a=int(input("Voulez-vous avancer de 1, 2, 3 ou 4 cases ? Tapez '1' , '2' , '3' ou '4"))
        while a>4 or a<=0:
            a=int(input("Voulez-vous avancer de 1, 2, 3 ou 4 cases ? Tapez '1' , '2' , '3' ou '4'"))
        joueur.avance(a)
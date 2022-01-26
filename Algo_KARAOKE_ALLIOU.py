class Player :
    def __init__(self, pseudo, numero, score, talent):
        self.__nom = pseudo
        self.__numero = numero
        self.__distance = score
    def getLook(self):
        return "@" + self.__numero
    def score(self):
        return self._score
    def talent(self) :
        return self.talent



Joueur1 = Player ("Didier", "Dédé", "1", "0", "1")
Joueur2 = Player ("Odette", "Ody", "2", "0", "5")
Joueur3 = Player ("Michelle", "Michou", "3", "0", "2")
Joueur4 = Player ("Jean-Claude", "J-C", "4", "0", "3")



while (Joueur1.score() > 50) :
    choix = int(input("Que fait le premier joueur? 1. Chanter la chanson A  2. Chanter la chanson B  3. Chanter la chanson C  4.Chanter la chanson D"))
    if (choix == 1) :
        Joueur1.score() + 50
    elif (choix == 2) :
        Joueur1.score() + 50
    elif (choix == 3) :
        Joueur1.score() + 60
    elif (choix == 4) :
        Joueur1.score() + 50

while (Joueur2.score() > 50) :
    choix = int(input("Que fait le second joueur? 1. Chanter la chanson A  2. Chanter la chanson B  3. Chanter la chanson C  4.Chanter la chanson D"))
    if (choix == 1) :
        Joueur2.score() + 80
    elif (choix == 2) :
        Joueur2.score() + 70
    elif (choix == 3) :
        Joueur2.score() + 60
    elif (choix == 4) :
        Joueur2.score() + 90

while (Joueur3.score() > 50) :
    choix = int(input("Que fait le troisième joueur? 1. Chanter la chanson A  2. Chanter la chanson B  3. Chanter la chanson C  4.Chanter la chanson D"))
    if (choix == 1) :
        Joueur3.score() + 50
    elif (choix == 2) :
        Joueur3.score() + 70
    elif (choix == 3) :
        Joueur3.score() + 60
    elif (choix == 4) :
        Joueur3.score() + 50

while (Joueur4.score() > 50) :
    choix = int(input("Que fait le quatrième joueur? 1. Chanter la chanson A  2. Chanter la chanson B  3. Chanter la chanson C  4.Chanter la chanson D"))
    if (choix == 1) :
        Joueur4.score() + 80
    elif (choix == 2) :
        Joueur4.score() + 70
    elif (choix == 3) :
        Joueur4.score() + 60
    elif (choix == 4) :
        Joueur4.score() + 50


while (Joueur1.score() < 50) :
    int(input("Votre score est au plus bas, Dédé !"))

while (Joueur2.score() < 50) :
    int(input("Votre score est au plus bas, Ody !"))

while (Joueur3.score() < 50) :
    int(input("Votre score est au plus bas, Michou !"))

while (Joueur4.score() < 50) :
    int(input("Votre score est au plus bas, J-C !"))





while (Joueur1.score() = 100) :
    choix = int(input ("Le joueur 1 a gagné ! Que voulez faire ? 1. Recommencer une partie 2. Arrêter"))
        if (choix == 1) :
            print("...")
        else :
            print("A bientôt !")

while (Joueur2.score() = 100) :
    choix = int(input ("Le joueur 2 a gagné ! Que voulez faire ? 1. Recommencer une partie 2. Arrêter"))
        if (choix == 1) :
            print("...")
        else :
            print("A bientôt !")

while (Joueur3.score() = 100) :
    choix = int(input ("Le joueur 3 a gagné ! Que voulez faire ? 1. Recommencer une partie 2. Arrêter"))
        if (choix == 1) :
            print("...")
        else :
            print("A bientôt !")

while (Joueur4.score() = 100) :
    choix = int(input ("Le joueur 4 a gagné ! Que voulez faire ? 1. Recommencer une partie 2. Arrêter"))
        if (choix == 1) :
            print("...")
        else :
            print("A bientôt !")




class Karaoke :
    def __init__(self, victoire, défaite, score):
        self.__distance = score
    def getName(self):
        return self.__victoire 
    def getLook(self):
        return "@" + self.__défaite
    def score(self):
        return self._score




class Chanson :
    def __init__(self, pseudo, numero, score, difficulte):
        self.__nom = pseudo
        self.__numero = numero
        self.__distance = score
        def getName(self):
        return self.__nom
    def getLook(self):
        return "@" + self.__numero
    def score(self):
        return self._score
    def difficulte :
        return self.difficulte

    
Chanson1 = Chanson ("Chanson 1", "Allumer le feu", "1", "30", "3")
Chanson2 = Chanson ("Chanson 2", "J'en parlerai au diable", "20", "2")
Chanson3 = Chanson ("Chanson 3", "Always", "3", "10", "1")
Chanson4 = Chanson ("Chanson 4", "Le Penitencier", "4", "40", "5")

while Player :
    choix = int(input("Vous participez à un karaoké. Vous avez possibilité de choisir la chanson que vous allez chanter. 1.A  2.B  3.C  4.D"))
        if (choix == 1) :
            print ("Vous avez choisi la chanson Allumer le feu !")
        elif (choix == 2) :
            print ("Vous avez choisi la chanson J'en parlerai au diable !")
        elif (choix == 3) :
            print ("Vous avez choisi la chanson Always !")
        elif (choix == 4) :
            print ("Vous avez choisi la chanson Le Pénitencier !")
        elif (choix == 5) :
            print ("Vous choisissez une chanson de façon aléatoire.")
            import random
            print(random.randrange(1,4)
























class Chapitre :
    def __init__(self, gold, hp, txt, links) :
        self.__orGagne = gold
        self.__pvPerdus = hp
        self.__texte = txt
        self.__listeLiens = links
    def getOrGagne(self):
        return self.__orGagne
    def getPvPerdus(self) :
        return self.__pvPerdus
    def getTexte(self) :
        return self.__texte
    def getListeLiens(self) 
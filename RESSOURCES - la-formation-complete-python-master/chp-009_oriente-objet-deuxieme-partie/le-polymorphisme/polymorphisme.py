"""_EXPLICATION : 
Le polymorphysme = on doit pouvoir utiliser les methodes de la meme facon sur tous les objets d'une meme entité.
On veut utiliser la methode mere pour tous. on passe donc par la surchagre pour pouvoir le faire mais en ajoutant super() pour préciser qu"on garde aussi la methode mere.
On a le meme nom pour la methode, mais elle fait différentes actions


Dans cet exemple la methode avance ,'est apas redéfinit mais augmenter

"""

class Vehicule:
    def avance(self):
        print("Le véhicule démarre")

class Voiture(Vehicule):
    def avance(self):
        super().avance() #on appelle la methode mere
        print("La voiture roule")# on ajoute un epharse pour notre enfant

class Avion(Vehicule):
    def avance(self):
        super().avance()
        print("L'avion vol")

v = Voiture()
a = Avion()
v.avance()
a.avance()
    
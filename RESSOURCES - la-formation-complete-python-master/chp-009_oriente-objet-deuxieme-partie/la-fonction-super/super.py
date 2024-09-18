"""EXPLICATION :
La methode super permet d'appeler le parent snas mettre son nom (dans le cas où on est amener à changer le nom de la classe)

On remplace le nom de la classe parent par super()
ATTENTION : dans ce cas, il ne faut pas mettre le self

"""



projets = ["pr_GameOfThrones", "HarryPotter", "pr_Avengers"]
class Utilisateur:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def __str__(self):
        return f"Utilisateur {self.nom} {self.prenom}"

    def afficher_projets(self):
        for projet in projets:
            print(projet)

class Junior(Utilisateur):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom) 

paul = Junior("Paul", "Durand")
paul.afficher_projets()


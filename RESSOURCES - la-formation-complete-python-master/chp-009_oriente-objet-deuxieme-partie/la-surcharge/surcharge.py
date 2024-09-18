"""Explication : 
    La surcharge permet de récupréer un methode du parent et de la modifier.=>Elle sera écraser dans la classe enfant
    La methode parent reste toujours accessible da la classe mere
    C'est la methode enfants ui sera executer si on execute une instance de l'enfant.
    Nous permet de redéfinir seulement ce qui nous interesse
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

    def afficher_projets(self): # ON SURCHARGE LA METHODE DU PARENT
        for projet in projets:
            if not projet.startswith("pr_"):
                print(projet)

paul = Junior("Paul", "Durand")
paul.afficher_projets()


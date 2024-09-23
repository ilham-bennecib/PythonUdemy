import json
import os
import logging



dossier_courant = os.path.dirname(__file__)
chemin_liste = os.path.join(dossier_courant, "data","movies.json")

class Movie:
    def __init__(self,title):
        self.title=title.title()

    def __str__(self) -> str:
        return self.title
    
    def _get_movie(self):
        with open(chemin_liste, "r") as f:
            return json.load(f)
    
    def _write_movies(self, movies):
        with open(chemin_liste, "w") as f:
    # Charger le contenu du fichier JSON dans une variable
            json.dump(movies, f, indent=4)

    def add_to_movies(self):
        #recuprer le fichier json
        liste = self._get_movie()
            #verifier que le film n'y est pas
        if self.title not in liste:
            liste.append(self.title)
            self._write_movies(liste)
            return True
        else:
            logging.warning(f"le film {self.title} est déjà dans la liste ")
            return False
    
    def remove_from_movies(self):
        #recupererl al iste de film
        liste =  liste = self._get_movie()
        #verifier qu'il est dedans o pas   
        if self.title in liste:
            liste.remove(self.title)
            self._write_movies(liste)
            return True
        else:
            logging.warning(f"le film {self.title} n'est pas dans la liste ")
            return False
    

def get_movies():
        movies=[]
        with open(chemin_liste, "r") as f:
            liste = json.load(f)
            for e in liste:
                movies.append(Movie(e))
        print(movies)
        
    

if __name__ == "__main__":
    get_movies()
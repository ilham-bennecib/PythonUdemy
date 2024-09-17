# importer dataclass
from dataclasses import dataclass


@dataclass
class Voiture:
    # creer les instances essence=100,
    essence:int =100
    # methode afficher_reservoir qui affiche le nombre de litres
    def afficher_reservoir(self):
        print(f"la voiture contient {self.essence}L d'essence ")
    
           
    #  méthode roule avec un paramètre km (kilomètre) qui va faire avancer la voiture et vider petit à petit le réservoir (5L pour 100km) =>(km * 5) / 100
    def roule(self, km):
        self.essence=100
        if (self.essence-((km*5)/100))>0 and (self.essence-((km*5)/100)>10):
            self.essence=self.essence-((km*5)/100) 
            print("la voiture n'a plus d'essence ") 
            
        elif (self.essence-((km*5)/100))<=0 :
            print("vous n'avez plus d'essence faites le plein")
            return
        self.afficher_reservoir()
    
    def faire_le_plein(self):
        self.essence=100
        print("vous pouvez repartir")
    

if __name__ == "__main__":
        v=Voiture()
        
        v.roule(1000)
    
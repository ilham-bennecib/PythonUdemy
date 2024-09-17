#fichier qui contiendra les classes
from dataclasses import dataclass

import logging
LOGGER = logging.getLogger()

@dataclass
class Liste(list):#on ajoute een parametre list pour que notre classe hérite des attribut
    nom: str
  
    #en utilisant dataclass, 'affichage de l'instance esr différente que celle souhaité. je dois donc redéfinir __repr__ pour un affichage personalisé  
    def __repr__(self):
        return f"Liste(nom='{self.nom}', contenu={super().__repr__()})"  #super().__repr__() est utilisé pour appeler la méthode de représentation de la classe parent (list), qui affiche le contenu de la liste.
 
    def ajouter(self, element):
        if not isinstance(element,str):# on verifie si l'element n'est pas une chaine de caractere
            raise ValueError("vous ne pouvez ajouter que des chaines de caractères")#on leve une erreur
        
        if element in self: #verifie sir l'element est dejà dans la liste
            LOGGER.error(f"{element} est dejà dans la liste")
            return False

        self.append(element)
        return True #permet de verifier si l'element a bien été ajouté. 
 
 
    def enlever(self, element) :
        if element in self:
            self.remove(element)
            return True
        
        return False
 
 
 
 #execution du code quand on est dans cette page   
if __name__ == "__main__":
        l=Liste("achat")
        l.ajouter("Pomme")
        l.ajouter("Pomme")
        l.enlever("Pomme")
        print(l)
   
        
        
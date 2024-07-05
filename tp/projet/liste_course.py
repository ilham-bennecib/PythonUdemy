#importer le module sys qui permetra de sortir du systeme
import sys

liste_course=[]
# demander à l'utilisateur de choisir parmi une de ces action en entrant un nombre de 1 à 5.

while True:
    action = input("Choisissez parmis les 5 options suivantes : \n 1 : Ajouter un élément à la liste de courses\n 2 : Retirer un élément de la liste de courses\n 3 : Afficher les éléments de la liste de courses\n 4 : Vider la liste de courses\n 5 : Quitter le programme\n Votre Choix : ")
    if not action.isdigit() in range(1,6):
            print("Veuillez entrer une action valide : ")
    elif int(action)==1:
          element_to_add = input("Entrez le nom d'un élment à ajouter à la liste de course : ")
          liste_course.append(element_to_add)
          print(f"L'element {element_to_add} a été ajouter à la liste")
          
    elif int(action)==2:
        element_to_remove = input("Entrez le nom de l'élment à retirer de la liste de course : ")
        if element_to_remove in liste_course:
            liste_course.remove(element_to_remove)
            print(f"L'element {element_to_remove} a bien été retirer de la liste")
        else : 
            print(f"L'element {element_to_remove} n'est pas dans la liste")
          
    elif int(action)==3:
          if len(liste_course)>=1:
                for i in liste_course:
                    print(f"{liste_course.index(i)+1} : {i}")
          else :
                print("la liste est vide")
    elif int(action)==4:
        liste_course.clear();
        print("la liste a été vidée de son contenu")
    elif int(action)==5:
         sys.exit()
        

        
                
       
            
          
        
          
        




# Bonne chance pour cet exercice ?

# Prends le temps de bien décrire toutes les étapes en français avant de te lancer dans le code !



# Quelques éléments pour t'aider :

# Pour boucler sur un itérable et récupérer en même temps l'indice de l'itération, tu peux utiliser la fonction enumerate :

# >>> for i, element in enumerate("Python"):
# >>>     print(i, element)
# 0 "P"
# 1 "y"
# 2 "t"
# 3 "h"
# 4 "o"
# 5 "n"
# Pour sortir d'un script en ligne de commande, tu peux utiliser le module sys et la fonction exit :

# import sys
# sys.exit()
# Cela aura pour effet de mettre fin au script en cours d'exécution.
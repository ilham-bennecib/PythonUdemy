import random
import sys


my_lives = 50
his_lives = 50
potions = 3

while my_lives>0 and his_lives>0:
    print(f"nombre de potion : {potions}")
    choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
# ?  Si l'utilisateur choisi la première option (1), vous infligez des points de dégât à l'ennemi.
    if choice=="1":
        my_attack = random.randint(5,10)
        his_lives = his_lives - my_attack
        print(f"Vous avez infliger {my_attack} de dégat à l'ennemi")
    elif choice=="2":
        if potions>0:  
            potion= random.randint(15,50)
            my_lives= my_lives+potion
            potions -=1
            print(f"Vous récupérez {potion} points de vie ({potions} potions restantes)")
            his_attack = random.randint(5,15)
            my_lives = my_lives - his_attack
            print(f"L'ennemi vous à infliger {his_attack} de dégat ")
            print(f"il vous reste {my_lives} points")
            print("-----------------------------------------")
            print(f"Vous passez votre tour...")
        else:
            print("Il ne vous reste plus de potion")
    else:
        choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

     
    his_attack = random.randint(5,15)
    my_lives = my_lives - his_attack
    print(f"L'ennemi vous à infliger {his_attack} de dégat ")
    print(f"il vous reste {my_lives} points")
    print(f"il reste {his_lives} points à votre adversaire")
    print("-----------------------------------------")  
if my_lives<=0 :
    print(f"Vous avez perdu. Fin du jeux")
        
elif his_lives<=0:
        print(f"Vous avez gagner. Fin du jeux")
sys.exit()     
    

# Ces points seront compris entre 5 et 10 et déterminés aléatoirement par le programme.

# ?  Si l'utilisateur choisi la deuxième option (2), vous prenez une potion.

# Les points de vie que la potion vous donne doivent être compris entre 15 et 50 et générés aléatoirement par le programme Python.

# Vous devez vérifier que l'utilisateur dispose de suffisamment de potion et décrémenter le nombre de potions qu'il a dans son inventaire lorsqu'il en boit une. Si l'utilisateur n'a plus de potions, vous devez lui indiquer et lui proposer de nouveau de faire un choix (attaquer ou prendre une potion).

# Quand le joueur prend une potion, il passe le prochain tour.

# Une fois l'action du joueur exécutée, et si l'ennemi est encore vivant, il vous attaque. Si l'ennemi est mort, vous pouvez terminer le jeu et indiqué à l'utilisateur qu'il a gagné ?

# L'attaque de l'ennemi inflige des dégâts au joueur compris entre 5 et 15, là encore déterminés aléatoirement par le script.

# Si vous n'avez plus de points de vie, le jeu se termine et vous avez perdu la partie.

# À la fin du tour, vous devez afficher le nombre de points de vie restants du joueur et de l'ennemi.

# Toutes ces opérations se répètent tant que le joueur et l'ennemi sont en vie.

# À chaque tour, vous attaquez en premier. Il ne peut donc pas y avoir de match nul. Si lorsque vous attaquez, votre attaque fait descendre les points de vie de l'ennemi en dessous (ou égal à) 0, vous gagnez la partie sans que l'ennemi n'ait le temps de vous attaquer en retour.
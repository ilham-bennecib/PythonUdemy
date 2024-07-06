import random 

r = random.randint(0,10)

tries = 5
print("Le jeu du nombre mystère ")
for i in range(0,5):
    
    
    print(f"il te reste {tries} essaies")
    nbr = input("Devine le nombre mystère entre 0 et 10 : ")
    if not nbr.isdigit():
        print("Veuillez entrer un nombre valide")
    
    
    else:
        if int(nbr) > r:
            tries +=-1 
            print(f"le nombre mystère est plus petit que {nbr}")
        elif int(nbr) == r:
            print("bravo tu as trouvé")
            break
        else:
            tries +=-1 
            print(f"le nombre mystère est plus grand que {nbr}")
if tries == 0:
    print(f"Le nombre mystère était {r}")
    
      
        
        
#importer random
import random
#voir quel fonctions existe dans ce module
print(dir(random))
#créer le 1er nombre entre 0 et 10 dans la variable a
a = random.randint(0,10)
#creer le 2nd nombre entre 0 et 10 dans la variable b
b = random.randint(0,10)
print(a, b)
#si a est plus garnd que b
if a>b:
    #afficher Le nombre a est plus grand que le nombre b.
    print ("Le nombre a est plus grand que le nombre b.")
#et si a = b
elif a==b:
    #afficher "Le nombre a et le nombre b sont égaux."
    print ("Le nombre a et le nombre b sont égaux.")
else:
    #afficher Le nombre a est plus petit que le nombre b.
    print ("Le nombre b est plus grand que le nombre a.")
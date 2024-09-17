# creation du chemin pour sauvegarder la liste
import os

CUR_DIR = os.path.dirname(os.path.abspath(__file__)) #retourne le nom du dossier du script actuel selon son chemin absolu
DATA_DIR = os.path.join(CUR_DIR, "data") #concatene la variable CUR_DIR avec la cahine de caractere "data". c'est un dossier dans lequel on stockera les donnés de la liste
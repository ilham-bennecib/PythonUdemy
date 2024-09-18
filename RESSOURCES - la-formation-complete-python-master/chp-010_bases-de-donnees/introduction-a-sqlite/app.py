import sqlite3 # le module est dejà dans python, pas besoin de le telecharger. disponible à l'import


conn = sqlite3.connect("database.db")# permet de se connecter au fichier database.db. si la bd n'existe pas, pyhton va automatiquement la créer
conn.close() # ferme la connection à la fin d'un fichier. pour pouvoir l'ouvrir à la mian plus tard
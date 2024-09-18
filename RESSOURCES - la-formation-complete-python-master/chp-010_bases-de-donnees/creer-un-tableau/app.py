import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor() # pour créer le tableau, o, abesoin d'un curseur. permet d'ex"cuter nos requetes sql. la requete est seulement créer

c.execute("""
CREATE TABLE IF NOT EXISTS employees(
    prenom text,
    nom text
)
""")
conn.commit()# enoyer à la base de donnée. ce n'est pas avec le curseur mais abvec la connexion qu'on fai le commit
conn.close()
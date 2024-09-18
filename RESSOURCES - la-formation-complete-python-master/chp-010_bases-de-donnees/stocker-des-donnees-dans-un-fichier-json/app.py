import json

fichier = "settings.json"

with open(fichier, "r") as f: # ici on lis le fichier json
    settings = json.load(f) # on demande a recuprér rle contenu dans une variable settings

settings["fontSize"] = 15 # on reaffecte la valeur de fontSize dans la varibale settings (et non le fichier)

with open(fichier, "w") as f: # on affecte la varibale stting modifiée dans le fichier settings
    json.dump(settings, f, indent=4)

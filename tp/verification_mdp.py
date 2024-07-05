mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_trop_court = "votre mot de passe est trop court."

while True:
    mdp = input("Entrez votre mot de passe : ")
    if len(mdp)==0 or mdp=="":
     print (mdp_trop_court.upper())
    elif len(mdp)<8:   
        print (mdp_trop_court.capitalize())
    elif mdp.isdigit():
        print("Votre mot de passe ne contient que des nombres.")
    else:
        print("Votre mot de passe est valide")
        break
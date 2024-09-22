from dataclasses import dataclass
import re #regex
import string

@dataclass
class User:
    first_name: str
    last_name: str
    phone_number: str =""
    address: str =""

    #la représentaion de nos instances
    def __repr__(self):
        return f"User({self.first_name}, {self.last_name})"
    
    #affichage de nos instances
    def __str__(self):
        return f"{self.full_name}\n{self.phone_number}\n{self.address}"

    #la proriété est dynamique != si on l'avait initialisé en attribut
    #cette propriété est recalculé à chaque fois à partir des valeurs misse à jour
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    #creation de methode de verification du forlat du tel
    #on ajoute le _ pour identid*fer cette méthode en privé, non accessible aux utilisateurs
    def _check_phone_number(self):
        phone_digit=re.sub(r"[+()\s]*","", self.phone_number)#regex : on cherche les+()et espace un nombre indefini de fois
        if len(phone_digit)<10 or not phone_digit.isdigit():
            raise ValueError(f"Le num de tel {self.phone_number} est invalide.")
        else:
            print(phone_digit)

    def _check_names(self):
        if not (self.first_name and self.last_name):
            raise ValueError("les nom et prenom ne peuvent pas être vides")
       
        
    

if __name__ == "__main__":
    from faker import Faker
    fake = Faker(locale="fr_FR")
    for _ in range(10):
        user = User(
                    fake.first_name(),
                    fake.last_name(),
                    fake.phone_number(),
                    fake.address()
                    )
        user._check_names()
        print("-"*10)
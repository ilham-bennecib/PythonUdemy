from faker import Faker

def get_user():
    fake = Faker()
    return f"{fake.first_name()} {fake.last_name()}"

# if __name__ == "__main__":
#     print(get_user())
    
def get_users(number_of_users):
    # solution 1 :  boucle (ATTENTION AJOUTER UN RETURN)
    # list_user=[]
    # for i in range(number_of_users):
    #      list_user.append(get_user())
    # return list_user
    
    # solution2: comprehension d liste
    
    return [get_user() for _ in range(number_of_users)]

if __name__ == "__main__":
    print(get_users(3))

"""
def greet_user():
    print("Hello")

greet_user()

"""
"""
def greet_user(username):
    print("Hello " + username)

greet_user('Jose')

"""
# 키워드 매개변수. 키-값 쌍을 넘김

def desc_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("my " + animal_type + "\'s name is " + pet_name + ".")

desc_pet(animal_type='hamster', pet_name='Harry')

# 매개변수 기본값 설정

def desc_pet2(pet_name, animal_type = 'dog'):
    print("\nI have a " + animal_type + ".")
    print("my " + animal_type + "\'s name is " + pet_name + ".")

desc_pet2(pet_name='Willy')
desc_pet2('Willy')
desc_pet2(pet_name='Jerry', animal_type='Cat')
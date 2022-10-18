from email import message
from multiprocessing.dummy import current_process


prompt = "\n tell me"
prompt += "\n enter 'quit' \t"

"""
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
    if message == 'quit':
        exit()

"""
"""
active_state = True

while active_state:
    message = input(prompt)

    if message == 'quit':
        active_state = False
    else:
        print(message)

"""
"""
current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 ==0:
        continue
    print(current_number)

"""

unconfirmed_users = ['alice', 'brian', 'Candace']
confirmed_users = []

while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    print("Verifing... " + current_users.title())
    confirmed_users.append(current_users)

print("confirmed: \n")

for confirmed_user in confirmed_users:
    print(confirmed_user.title()) 

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

responses = {}

polling_active = True

while polling_active:
    name = input("Enter your name > ")
    response = input("Mountain? > ")
    responses[name] = response
    
    repeat = input("another person?(y/n) \n")
    if repeat.title() == 'N':
        polling_active = False
    
print("\n --------------reults")

for name, response in responses.items():
    print(name + " another " + response)

print(responses)
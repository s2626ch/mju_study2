from multiprocessing.dummy import current_process


def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title()
        print(msg)

user_names = ['hannah', 'ty', 'margot']
greet_users(user_names)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)

print("\nPrinted are ")
for completed_model in completed_models:
    print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("completed: ")
    for completed_model in completed_models:
        print(completed_model)


print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

def make_pizza(*toppings):
    print("\ntoppings: ")
    for topping in toppings:
        print(topping)
    
make_pizza('pp')
make_pizza('pp', 'qq')
def make_pizza2(size, *toppings):
    print("\nMaking " + str(size) + " inch pizza with ")
    for topping in toppings:
        print(topping)

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    
    for key, value in user_info.items():
        profile[key] = value
    return profile

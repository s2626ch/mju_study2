# 빈튜플을 매개변수로 받아서 자유롭게 사용
def make_pizza(*toppings):
    
    print(toppings)

make_pizza('pp')
make_pizza('pp', 'qq')

#위치형 매개변수와 임의의 매개변수 함께 쓰기

def make_pizza2(size, *toppings):
    print("\nMaking " + str(size) + " inch pizza with ")
    for topping in toppings:
        print(topping)

make_pizza2(16, 'pp')
make_pizza2(12, 'qq', 'pp')

#임의의 키워드 매개변수 사용

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('alber', 'einstein', location = 'princeton', field = 'physics')
print(user_profile)
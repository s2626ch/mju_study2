
# json 파일 쓰기

"""

import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'number.json'

with open(filename, 'w') as f_obj:
    # json파일에 쓰기
    json.dump(numbers, f_obj)

"""

#json 파일 읽기
"""
import json

filename = 'number.json'

with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)

"""

#데이터 저장하고 읽기
"""
import json

filename = 'username.json'

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input('> ')
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("your name is  " + username)
else:
    print("Welcome back " + username)

"""

#데이터 저장하고 읽기 개선버전

import json

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("> ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print("Welcoem " + username)
    else:
        username = get_new_username()
        print("OK " + username)

greet_user()

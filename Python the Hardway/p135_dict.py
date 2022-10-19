favorite_languages = {
    'jen': 'python',
    'sara': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print(f"Sara의 favirite language는 '{favorite_languages['sara'].title()}'입니다.")
print("======================================")

for name, language in favorite_languages.items():
    print(name.title() + '\'s favorite language is ' + language.title())

print("======================================")

for name in favorite_languages:
    print(name.title())

print("======================================")

for name in sorted(favorite_languages):
    print(name.title())

print("======================================")

friends = ['phil', 'sara']

for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("Hi, " + name.title() + " Your favorites is " + favorite_languages[name].title())

print("======================================")

for language in sorted(favorite_languages.values()):
    print(language.title())

print("======================================")

for language in sorted(set(favorite_languages.values())):
    print(language.title())

print("======================================")
print("딕셔너리 내에 리스트 담기")

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sara': ['c',],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskel'],
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorites languages are ")
    for language in languages:
        print(language + " ")

print("======================================")
print("딕셔너리 내에 딕셔너리 담기")

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for user_name, user_info in users.items():
    print("\nUsername: " + user_name)
    full_name = user_info['first'] + user_info['last'] 
    location = user_info['location']
    print("\tfullname:" + full_name.title())
    print("\tlocation: " + location)
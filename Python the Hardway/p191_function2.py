def get_formatted_name(first_name, last_name, middle_name = ''):
    
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    
    return full_name.title()

musician = get_formatted_name('Jimi', 'Hendrix')
print(musician)

musician = get_formatted_name('John', 'Hooker', "lee")
print(musician)


# 함수에서 딕셔너리 반환
def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('Jimi', 'Hendrix', age=27)
print(musician)

while True:
    print("\nPlease tell me your name")
    print("enter 'q' to quit")

    f_name = input("First Name ")
    if f_name == 'q':
        break
    l_name = input("Last_name ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello " + formatted_name)

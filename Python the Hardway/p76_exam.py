from msilib.schema import BBControl


invite_dinner = ['a', 'b', 'c', 'd', 'e', 'f']

for person in invite_dinner:
    print("Welcome " + person)
print("-----------------")

invite_dinner[1] = 'bb'

for person in invite_dinner:
    print("Welcome " + person)

print("-----------------")

invite_dinner.insert(0, 'aa')
invite_dinner.insert(3, 'cc')
invite_dinner.append('g')

no = 1
for person in invite_dinner:
    print(str(no))
    print(" Welcome " + person)
    no += 1
print("-----------------")

print("Sorry")
print(str(len(invite_dinner)))

for person in range(0, len(invite_dinner)-2):
    invite_dinner.pop()

no = 1
for person in invite_dinner:
    print(str(no))
    print(" Welcome " + person)
    no += 1
print("-----------------")

print("Sorry, Del all")


for i in range(0,2):
    del invite_dinner[i]

print("-----------------")
print(invite_dinner)

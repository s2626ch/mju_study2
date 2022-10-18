# 0나누기 예외처리

"""
print("Give me a number")
print("\nq for quit")

while True:
    first_num = input("\n First Number ")
    if first_num == 'q':
        break

    second_num = input("\n Second Number ")
    if second_num == 'q':
        break
    
    try:
        answer = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print("input 0!")
    else:
        print(answer)



# 파일 예외

filename = 'alice.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "No file"
    print(msg)

"""

#파일 내 단어 수 카운드
"""
filename = 'alice.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "No file"
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print("word count" + str(num_words))

"""
# 개선 버전

def count_words(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = "No file"
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("This file " + filename + 'has ' word count" + str(num_words)) 

filename = 'alice.txt'
filenames = [alice.txt]


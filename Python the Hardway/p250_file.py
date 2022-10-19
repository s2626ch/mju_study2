"""
#with를 사용하면 close() 사용할 필요 없음
with open('pi_million_digits.txt') as file_object:
    #read()는 EOF에서 빈문자열 반환
    contents = file_object.read()
    print(contents.rstrip())
"""

"""
#파일 한줄씩 읽기
file_name = 'pi_million_digits.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line)
"""

#파일을 with 블록에서 일괄적으로 읽고 블록 밖에서 처리하기
"""
file_name = 'pi_million_digits.txt'
with open(file_name) as file_object:
    #파일의 행들을 리스트로 저장
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

"""
# 파일의 숫자를 공백없이 하나의 문자열로 만들기
"""
file_name = 'pi_million_digits.txt'
with open(file_name) as file_object:
    #파일의 행들을 리스트로 저장
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
"""

# pi안에 자기 생일이 있는지 찾기

file_name = 'pi_million_digits.txt'
with open(file_name) as file_object:
    #파일의 행들을 리스트로 저장
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.rstrip()

birthday = input("(mmddyy)> ")
if birthday in pi_string:
    print("birthday appears" )
else:
    print("birthday not appears")
    
print(pi_string.find(birthday))
print(pi_string.rfind(birthday))

# 파일 새로 만들고 쓰기

filename = 'programming.txt'
with open(filename, 'w') as file_object:
    # write 함수는 한줄 쓰기 함수. 개행 안함. 개행하려면 \n 추가
    file_object.write("I live prog.\n")
    file_object.write(" So what?\n")

# 파일 이어 붙이기 'a'
with open(filename, 'a') as file_object:
    # write 함수는 한줄 쓰기 함수. 개행 안함. 개행하려면 \n 추가
    file_object.write("You live prog.\n")
    file_object.write(" So what?")


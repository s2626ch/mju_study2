# -*- coding: utf-8 -*-

from sys import argv

script, file_name = argv
print(f"{file_name}을 지우려고 합니다.")
print("취소하시려면 CTRL-C(^C)를 눌러주세요")
print("진행하려면 리턴키를 누르세요")

input("???")
print("파일을 여는 중...")
dest = open(file_name, 'w', encoding='utf-8')

print("파일 내용을 지웁니다. 안녕히!")
# dest.truncate()

print("이제 세 줄에 들어갈 내용을 부탁드릴께요")

line1 = input("1 줄: ")
line2 = line1 + '\n' + input("2 줄: ")
line3 = line2 + '\n' + input("3 줄: ")

print("이 내용을 파일에 씁니다")

dest.write(line3)
dest.write("\n")

print("파일을 닫습니다.")
dest.close()
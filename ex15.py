# -*- coding: utf-8 -*-

from sys import argv

script, file_name = argv
text = open(file_name, encoding = 'utf-8')
print(f"파일 {file_name}의 내용")
print(text.read())

print("파일 이름을 다시 입력해 주세요")
file_onemore = input("> ")
text_onemore = open(file_onemore, encoding='utf-8')
print(text_onemore.read())
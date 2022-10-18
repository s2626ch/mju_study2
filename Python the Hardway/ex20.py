# -*- coding: utf-8 -*-

from sys import argv

script, input_file = argv

def print_all(file):
    print(file.read())

def rewind(file):
    file.seek(0)

def print_oneline(line_cnt, file):
    print(line_cnt, file.readline())

cur_file = open(input_file, encoding='utf-8')

print("파일 전체를 출력해봅시다.\n")
print_all(cur_file)

print("되감아 봅시다")

rewind(cur_file)

print("세 줄을 출력해 봅시다")
cur_line_cnt = 1
print_oneline(cur_line_cnt, cur_file)

cur_line_cnt = cur_line_cnt + 1
print_oneline(cur_line_cnt, cur_file)

cur_line_cnt = cur_line_cnt + 1
print_oneline(cur_line_cnt, cur_file)


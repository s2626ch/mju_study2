from sys import argv

script, input_file = argv

def print_All(file):
    print(file.read())

def rewind(file):
    file.seek(0)

def print_Oneline(line_cnt, file):
    print(line_cnt, file.readline())

cur_file = open(input_file, encoding='utf-8')
print("파일 전체 출력 \n")
print_All(cur_file)
print("되감아 봅시다 \n")
rewind(cur_file)
print("세 줄을 출력해 봅시다 \n")

cur_line_cnt = 1
print_Oneline(cur_line_cnt, cur_file)

cur_line_cnt = cur_line_cnt + 1
print_Oneline(cur_line_cnt, cur_file)

cur_line_cnt = cur_line_cnt + 1
print_Oneline(cur_line_cnt, cur_file)

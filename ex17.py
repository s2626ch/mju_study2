# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

script, src_file, dest_file = argv

print(f"{src_file}에서 {dest_file}로 복사합니다")

input_file = open(src_file, encoding='utf-8')
input_data = input_file.read()

print(f"입력 파일은 {len(input_data)}바이트입니다.")
print(f"출력 파일이 존재하나요? {exists(dest_file)}")
print("준비되었습니다. 계속하려면 리턴을 취소하시려면 CTRC-C를 누르세요.")
input('_>')

output_file = open(dest_file, 'w', encoding='utf-8')
output_file.write(input_data)
print("모두 완료되었습니다")

output_file.close()
input_file.close()
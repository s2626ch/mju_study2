# -*- coding: utf-8 -*-

from sys import argv

# argv  unpack --> 실행인자 전체를 한 변수에 담는 것이 아니라 네 개의 변수에 '풀어 놓음'
스크립트, 첫번째, 두번째, 세번째 = argv

print("스크립트 이름: ", 스크립트)
print("첫번째: ", 첫번째)
print("두번째: ", 두번째)
print("세번째): ", 세번째)
﻿def 둘출력(*args):
    실행인자1, 실행인자2 = args
    print(f"실행인자1: {실행인자1}, 실행인자2: {실행인자2}")

def 둘출력다르게(실행인자1, 실행인자2):
    print(f"실행인자1: {실행인자1}, 실행인자2: {실행인자2}")

def 하나출력(실행인자1):
    print(f"실행인자1: {실행인자1}")

def 영출력():
    print("아무것도 안 받음")

둘출력('제드', '쇼')
둘출력다르게('제드', '쇼')
하나출력('하나')
영출력()
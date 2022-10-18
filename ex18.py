# -*- coding: utf-8 -*-

def two_out(*args):
    param1, param2 = args
    print(f"실행인자1:{param1}실행인자2:{param2}")

def two_out2(param1, param2):
    print(f"실행인자1:{param1}실행인자2:{param2}")

def one_out(param1):
    print(f"실행인자1:{param1}")

def zero_out():
    print("nothint1")

two_out('제드', '쇼')
two_out2('제드', '쇼')
one_out('하나')
zero_out()
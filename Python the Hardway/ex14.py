﻿# -*- coding: utf-8 -*-

from sys import argv

스크립트, 사용자이름 = argv
프롬프트 = '> '

print(f"안녕 {사용자이름}, 나는 {스크립트}야.")
print("몇 가지 질문을 할 께")
print(f"{사용자이름}, 나 좋아해?")
좋아 = input(프롬프트)

print(f" {사용자이름}, 어디에 살아")
살아 = input(프롬프트)

print("무슨 컴퓨터를 가지고 있지?")
컴퓨터 = input(프롬프트)

print(f"""
좋아, 나를 좋아하냐는 질문에는 \'{좋아}\', 
{살아}에 살아. 어딘지는 모르겠지만, 
그리고 {컴퓨터} 컴퓨터를 가졌어. 근사한걸. 
""")
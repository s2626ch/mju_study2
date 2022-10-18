# -*- coding: utf-8 -*-

print("모든 것을 연습해 봅시다.")
print('\\를 이용해 \n\ 새줄이나 \t  탭을 하는 탈출 문자열에 대해 \'알아야만\' 합니다.')

poet = """
\t the lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion
and requires an explanation
\n\t \t where there is none

"""

print("--------------------------")
print(poet)
print("--------------------------")

five = 10 - 2 + 3 - 6
print(f"이 값은 다섯입니다: {five}")

def secret_exp(start):
    jelly = start * 500
    bowl = jelly /1000
    box = bowl /100
    return jelly, bowl, box

start_point = 10000
jelly, bowl, box = secret_exp(start_point)

print("시작점: {}".format(start_point))
print(f"젤리 {jelly}알, {bowl} 그릇, {box}상자가 있습니다.")

start_point = start_point / 10
print("이렇게 할 수도 있습니다.")
exp = secret_exp(start_point)
print("젤리: {}알, {}그릇, {}상자".format(*exp))
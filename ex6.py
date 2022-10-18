# -*- coding: utf-8 -*-

kind = 10
x = f"세상에는 {kind}종류의 사람이 있어요."
binary = "'이진수'"
unknown = "모르는"

y = f"{binary}아는 사람과 {unknown} 사람."

print(x)
print(y)

print (f"'{x}'라고 했어요.")
print (f"'{y}'이라고도 했어요.")

funny = False
joke_eval = "웃기는 농담 아니예요? {}"
print(joke_eval.format(funny))

w = "이 문자열의 왼쪽 -->"
e = "<--이 문자열의 오른쪽"

print(w + e)
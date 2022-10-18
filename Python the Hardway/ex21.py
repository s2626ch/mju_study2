# -*- coding: utf-8 -*-

def plus(a,b):
    # print(f"plus {a} + {b}")
    print("plus: ", a + b)
    return a + b

def minus(a,b):

    #print(f"minus {a} - {b}")
    print("minus: ", a - b)
    return a - b

def multiply(a,b):
    # print(f"multiply {a} * {b}")
    print("multiply: ", a * b)
    return a * b

def divide(a,b):
    # print(f"minus {a} / {b}")
    print("divde: ", a / b)
    return a / b

print("함수만으로 계산해 봅시다!")

age = plus(30, 5)
height = minus(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"나이: {age}, 키:{height} 몸무게: {weight}, 아이큐:{iq}")

print("추가 문제")

value = plus(age, minus(height, multiply(weight, divide(iq, 2))))
print(f"결과: ", value, "손으로 계산할 수 있나요?")

v1 = divide(iq, 2)
print(v1)

v2 = multiply(weight, v1)
print(v2)

v3 = minus(height-v2)
print(v3)


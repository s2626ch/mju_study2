
numbers = []

def callWhile(i, number, j):
    while i < number:
        print(f"꼭대기에서 노는 {i}")
        numbers.append(i)

        i = i + j
        print("숫자는 이제", numbers)
        print(f"바닥에서 노는 {i}")

callWhile(1, 6, 1)

print("숫자: ")

for number in numbers:
    print(number)


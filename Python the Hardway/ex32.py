# 리스트 생성
numbers = [1, 2, 3, 4, 5]
fruits = ['사과', '귤', '배', '살구']
changes = [1, '십원', 2, '백원', 3, '오백원']

for number in numbers:
    print(f"이 수는 {number}")

for fruit in fruits:
    print(f"과일종류 {fruit}")

for i in changes:
    print(f"받은 잔돈 {i}")

elements = []

for i in range(0,6):
    print(f"리스트에 {i} 숫자를 더합니다.")
    elements.append(i)

for i in elements:
    print(f"원소는 {i}")
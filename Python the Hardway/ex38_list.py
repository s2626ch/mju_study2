열_가지 = "사과 귤 까마귀 잔화기 빛 설탕"
print("고쳐 봅시다")

stuff = 열_가지.split(' ')
stuff2 = ["낯", "밤", "노래", "부메랑", "옥수수", "바나나", "아이", "어른"]

while (len(stuff)) != 10:
    next_one = stuff2.pop()
    print("추가:", next_one)
    stuff.append(next_one)
    print(f"이제 {len(stuff)}  항목이 있습니다.")

print("물건", stuff)

print("do something")
print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(stuff)
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
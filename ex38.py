ten = "apple orange crow telephone light sugar"
print("wait, fix this!")

# 문자열을 대상으로 sep 단위로 쪼갠 리스트를 반환한다.
sutff = ten.split(' ')
other_stuff = ["day", "night", "song", "voomerang", "corn", "banana", "child", "adult"]

while len(sutff) != 10:
    # 리스트의 마지막 항목을 뽑는다.
    next_one = other_stuff.pop()
    print("adds: ", next_one)
    sutff.append(next_one)
    print(f"now {len(sutff)}개 항목이 있습니다.")

print("let me see", sutff)
print("Let's do something.")

print(sutff[1])
print(sutff[-1])
print(sutff.pop())
# 리스트를 join을 통해 문자열로 만듬.
print(' '.join(sutff))
print(sutff[3:5])
print('#'.join(sutff[3:5]))
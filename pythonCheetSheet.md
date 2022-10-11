# 1. 리스트
## 리스트 생성

a = list()
b = []
c = [1, 2, 3]

print(c)
#### [1, 2, 3]

## 리스트 값 추가
c.append(4)

print(c)
#### [1, 2, 3, 4]

## 리스트에 값 삽입
### insert(index, value)
c.insert(3,5)

print(c)

##### [1, 2, 3, 5, 4]

## 리스트에 값 꺼냄

print(c[3])

##### 5

## 리스트의 특정한 범위의 값 가져오기: slicing

print(c[3:5])

##### [5, 4]

### index 3 이전까지
print(c[:3])
#### [1, 2, 3]

print(c[4:])
##### [4]

for i in range(len(c)):
    print(i, "->" ,c[i])
    
####     
'''
0 -> 1
1 -> 2
2 -> 3
3 -> 5
4 -> 4
'''
#### 인덱스 1~3까지의 값에서 마지막 인자를 통해 2step 점프
print(c[1:4:2])

'''
[2, 5]
'''

## 리스트 삭제
### 인덱스로 삭제는 del, 값 삭제는 remove
### 추출은 스택의 pop(index) -> 삭제될 값을 리턴하고 삭제

a = [1, 2, 3, 5, 4, '안녕', True]

### 1번 인덱스 삭제
del (a[1])

print(a)

'''
[1, 3, 5, 4, '안녕', True]

'''
#### 3이라는 값 삭제
a.remove(3)

print(a)

'''
[1, 5, 4, '안녕', True]
'''

b = a.pop(3)

print(a)
'''
print(a)
'''
[1, 5, 4, True]



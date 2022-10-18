from statistics import mean

"""
 리스트 함수
추가
append(): 리스트 끝에 항목 추가
insert(): 리스트 특정 위치에 삽입. insert
int PyList_Insert(PyObject *list, Py_ssize_t index, PyObject *item)
Insert the item item into list list in front of index index. Return 0 if successful; return -1 and set an exception if unsuccessful. Analogous to list.insert(index, item).

int PyList_Append(PyObject *list, PyObject *item)
Append the object item at the end of list list. Return 0 if successful; return -1 and set an exception if unsuccessful. Analogous to list.# 

append(item).

# 삭제
del(): del(list[index])
remove(): remove(list.remove(value))
pop(): 마지막 항목 제거


"""



even_numbers = list(range(2,11,2))
for even_number in even_numbers:
    print(even_number)
    
print("\n")

squares = []
values = list(range(1, 11, 2))
for value in values:
    square = value**2
    squares.append(square)
    print(value, "\t", square)
    print("---------------------")
    print(squares)
    print(f"이 데이터의 최소값은 {min(squares)}, 합계는 {sum(squares)}, 평균은 {mean(squares)}입니다." )
    print("====================")

#리스트 내포

squares2 =[value**3 for value in range(1, 11)]
print(squares2)
print("====================")

players = ['Charles', 'martina', 'michael', 'eli']

print("Three Members")

for player in players[:3]:
    print(player.title())

# 리스트 복사
# 슬라이스 없이 복사하면 같은 객체를 가리킨다. 

my_foods = ['pizza', 'falafel', 'carot cake']
friend_foods = my_foods[:]

print(f"내가 좋아하는 음식은 {my_foods}입니다.")
print(f"친구가 좋아하는 음식은 {friend_foods}입니다.")

print("====================")

my_foods.append('canoli')
print(f"내가 좋아하는 음식에 canoli 추가")
friend_foods.append('ice cream')
print(f"친구가 좋아하는 음식에 ice cream 추가")

print(f"내가 좋아하는 음식은 {my_foods}입니다.")
print(f"친구가 좋아하는 음식은 {friend_foods}입니다.")


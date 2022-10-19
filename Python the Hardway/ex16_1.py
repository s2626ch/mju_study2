from sys import argv

스크립트, 파일이름 = argv

print(f"{파일이름} 파일을 지우려 합니다")
print("취소하려면 CRRL-C(^C)를 누르세요")
print("진행하려면 리턴 키를 누르세요")

input("?")

print("파일 여는 중...")
목적지 = open(파일이름, 'w', encoding='utf-8')

print("파일 내용을 지웁니다. 안녕히!")
# 목적지.truncate()

print("이제 세 줄에 들어갈 내용을 입력하세요!")
줄1 = input('1줄:')
줄2 = input('2줄:')
줄3 = input('3줄:')

print("이 내용을 파일에 씁니다")
목적지.write(줄1 + '\n' + 줄2 + '\n' + 줄3 + '\n')

print("파일을 닫습니다")
목적지.close()
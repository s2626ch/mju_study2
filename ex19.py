# -*- coding: utf-8 -*-

def cheese_cracker(cheese_count, cracker_box):
    print(f"치즈가 {cheese_count}개 있어요!")
    print(f"크래커가 {cracker_box}상자 있어요!")
    print("파티 벌이기 충분하네")
    print("담요 한장 가져오삼")
    print("""
    
    """)

print("함수에 숫자를 바로 넣어 줄 수 있습니다")

cheese_cracker(20, 30)

print("스크립트의 변수를 쓸 수도 있어요.")
cheese_vol = 10
cracker_vol = 50

cheese_cracker(cheese_vol, cracker_vol)

print("안에서 계산 가능")
cheese_cracker(10 + 20, 5 + 6)
print("합쳐서 변수도 쓰고 계산도 합시다")
cheese_cracker(cheese_vol + 100, cracker_vol + 1000)

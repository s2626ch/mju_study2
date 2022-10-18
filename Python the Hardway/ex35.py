from sys import exit

def gold_room():
    print("황금으로 가득찬 방입니다. 얼마나 가져갈까요?")

    choice = input("> ")

    if "0" in choice or "1" in choice:
        amount = int(choice)
    else:
        death("인간이여. 숫자쓰는 법부터 배우시라.")

    if amount < 50:
        print("좋아. 욕심부리지 않는군. 당신이 이겼소.")
        exit(0)
    else:
        death("욕심쟁이에게 죽음을!")

def bear_room():
    print(""" 여기 곰이 한마리 있습니다.
    \t 곰은 꿀을 잔뜩 들고 있네요
    \t 뚱뚱한 곰은 다른 쪽 문 앞에 있습니다.
    \t 어떻게 곰을 움직이겠습니까?""")

    bear_moves = False

    while True:
        choice = input("선택지는 honey, playing, open입니다.> ")

        if choice == "honey":
            death("곰이 따귀를 때렸습니다")
        elif choice == "playing" and not bear_moves:
            print("곰이 문에서 비꼈습니다.")
            print("이제 나갈 수 있어요")
            bear_moves = True
        elif choice == "playing" and bear_moves:
            death("곰이 다리를 씹어 먹었습니다.")
        elif choice == "open" and bear_moves:
            gold_room()
        else:
            print("무슨 말을 하는 지 모르겠네요")


def ktulu_room():
    print(""" 여기서 크툴루를 봅니다.
    그 분이, 그것이 당신을 쳐다보고 당신은 미쳐갑니다.
    목숨을 위해 달아나려나 네 머리를 먹처치우려나?""")

    choice = input("선택지는 run, eat입니다. > ")

    if "run" in choice:
        start()
    elif "eat" in choice:
        death("맛있군")
    else:
        ktulu_room()

def death(reason):
    print(reason, "잘 했어요!")
    exit(0)

def start():
    print(""" 어두운 방에 있습니다.
    오른 쪽과 왼쪽에 문이 있습니다.
    어느 쪽을 고를까요?""")

    choice = input("선택지는 left, right입니다. > ")

    if choice == "left" :
        bear_room()
    elif choice == "right":
        ktulu_room()
    else:
        death("선택을 하지 않은 죄")

start()
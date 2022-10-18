print("""문이 두개 있는 어두운 방에 들어왔습니다.
1번과 2번 중 어느방에 들어갈까요?""")

door = input(">")

if door == "1":
    print("거대한 곰이 치즈 케익을 먹고 있습니다. ")
    print("무엇을 할까요?")
    print("1: 케이크를 뺏는다.")
    print("2: 곰에게 소리치기")

    bear = input(">")

    if bear == "1":
        print("거대한 곰이 머리를 먹어 치웁니다.")
    elif bear == "2":
        print("거대한 곰이 다리를 먹어 치웁니다.")
    else:
        print(f"음, {곰}행동을 하는 것이 더 나았나 보네요.")
        print("거대한 곰이 도망갑니다. ")

elif door == "2":
    print("당신은 크툴루 눈동자의 심연을 봅니다. ")
    print("1: 블루베리")
    print("2: 노란 재킷")
    print("3: 권총이 울부짖는 것.")

    madness = input(">")

    if madness == "1" or madness == "2":
        print("당신은 젤리 푸딩의 힘으로 살아남았습니다.")
        print("잘 했어요!")
    else:
        print("광기가 당신의 눈 너머로 파고 듭니다.")
        print("잘 했어요")
else:
    print("비틀거리다 심연에 몸을 던집니다. 잘 했소!")
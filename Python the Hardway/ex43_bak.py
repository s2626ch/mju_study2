from sys import exit
from random import randint
from textwrap import dedent

# Scene Class
# -> Death, Scentral_Corridor, Razor_Armory, Bridge, Lifeboat 클래스는 장면을 파라미터로 받는다.
# 이 클래스들은 각각의 enter 메소드를 수행한다.
# Enter Method
class Scene(object):
    def enter(self):
        print("아직 만들지 않은 장면입니다.")
        print("상속해서 enter()를 구현하세요.")
        exit(1)

#Engine Class
# scene_map parameter init
class Engine(object):
    def __init__(self, scene_map):
        self.scenemap = scene_map

# 사막 장면을 현재 장면, 마지막을 다음 장면으로 설정
    def play(self):
        cur_scene = self.scenemap.opening_scene()
        last_scene = self.scenemap.next_scene('TheEnd')

        while cur_scene != last_scene:
            print('32')
            last_scene_name = cur_scene.enter()
            cur_scene = self.scenemap.next_scene(last_scene_name)

        cur_scene.enter()

# 죽음 클래스.
# 죽을 때 나오는 대사를 랜덤으로 보여준다.
class Death(Scene):
    talks = [
        "사망. 진짜 못하네요",
        "어머니가 자랑스러워 하시겠어요.... 좀 더 똑똑했다면.",
        "패배자 같으니."
        "내가 기르는 강아지도 이거보단 잘 해요."
        "부장님이 개그를 해도 이거보단 잘하겠소."
    ]

    def enter(self):
        print(
            Death.talks[randint(0, len(self.talks)-1)])
        exit(1)

# 시작 메시지가 나온다.
# 사용자의 입력에 따라 결과를 보여준다.
class Central_Corridor(Scene):
    def enter(self):
        print(dedent("""
                페르칼 25번 행성의 고던 족은 모든 승무원을 죽였습니다...
                고던인이 뛰쳐 나오는 동안 당신은 중앙복도에서 무기고로 내달리고 있습니다. 
                고던인은 무기고로 가는 문을 가로막고 당신에게 무기를 겨누는 참입니다. 
        """))

        action = input("> ")

        if action=="fire":
            print(dedent("""
                    당신을 고던인을 쏘아버립니다.... 그러나 결국 고던인은 당신을 먹어치웁니다.
            """))
            return 'Death'

        elif action == "escape":
            print(dedent("""
                     광선총이 빗겨납니다. 그러나 결국 고던인을 당신을 잡아먹을 뿐입니다. 
            """))
            return 'Death'

        elif action == "joke":
            print(dedent("""
                     당신은 고던인이 웃는 동안 머리를 맞추고 무기고의 문으로 뛰어듭니다. 
            """))
            return 'Razor_Armory'

        else:
            print("처리할 수 없습니다.")
            return 'Central_Corridor'

class Razor_Armory(Scene):
    def enter(self):
        print(dedent("""
                        당신은 무기고로 뛰어들어 방을 살핍니다... 
                        보관함은 잠겨있고 당신은 3자리 비밀번호를 알아내야 합니다. 
                """))
        #비밀번호 3자리 난수 생성
        code = f"{randint(1,9)}{randint(1,9), randint(1,9)}"
        guess = input("비밀번호 세자리를 입력하세요 >")
        guess_cnt = 1

        while (guess != code and guess_cnt <10):
            print("Oops!")
            guess_cnt += 1
            guess = input(f"현재 {guess_cnt} 번째 입니다. 비밀번호 세자리를 입력하세요 >")

        if guess == code:
            print(dedent("""
                    보관함이 열리자 공기가 새어나옵니다. 중성자탄을 들고 함교로 내달립니다. 
            """))
            return 'Bridge'
        else:
            print(dedent("""
                           마지막 기회를 지나자 폭탄이 터집니다.
                        """))
            return 'Death'

class Bridge(Scene):
    def enter(self):
        def enter(self):
            print(dedent("""
                           당신은 함교로 뛰어들었습니다. 고던인들은 아직 무기를 뽑지 않았습니다.  
                        """))
            action = input("> ")

            if action == "bomb":
                print(dedent("""
                                당신은 폭탄을 집어 던집니다. 그러나 총에 맞습니다. 
                                당신은 죽어가는 동안 폭탄이 터지기를 바랍니다만...  
                                        """))
                return 'death'

            elif 'action' == 'install':
                print(dedent("""
                                당신은 폭탄을 설치합니다. 그리고 밖으로 뛰어나가 잠금잠치를 부숩니다. 
                                그리고 구명정으로 달려갑니다.   
                            """))
                return 'life_boat'
            else:
                print("처리할 수 없습니다. ")
                return 'Bridge'

class Lifeboat(Scene):
    def enter(self):
        def enter(self):
            def enter(self):
                print(dedent("""
                                당신은 구명정으로 달립니다. 구명정은 5대가 있습니다. 몇번을 타시겠습니까?
                            """))
                lifeboat = randint(1,5)
                guess = input("[구명정 번호]> ")

                if int(guess) != lifeboat:
                    print(dedent(f"""
                            {guess}번 구명정으로 들어가 탈출 단추를 누릅니다. 
                                    구명정은 우주로 나아가자 마자 구명정이 폭발합니다. 
                                    """))
                    return 'Death'

                else:
                    print(dedent(f"""
                            {guess}번 구명정으로 들어가 탈출 단추를 누릅니다. 
                            구명정은 아래의 행성으로 나아갑니다. 뒤를 돌아보자 우주선이 폭발하는 것을 봅니다.                               
                                 """))
                    return 'TheEnd'

class TheEnd(Scene):
    def enter(self):
        print("승리했습니다!")
        return 'TheEnd'

class Map(object):
    scenes = {'Central_Corridor': Central_Corridor(), 'Razor_Armory': Razor_Armory()
              , 'Bridge': Bridge(), 'LifeBoat': Lifeboat(), 'Death': Death(), 'End': TheEnd() }
    def __init__(self, start_scene):
        self.startscene = start_scene
    def next_scene(self, scene_name):
        next = Map.scenes.get(scene_name)
        return next
    def opening_scene(self):
        return self.next_scene(self.startscene)

game_map = Map('Central_Corridor')
game_engine = Engine(game_map)
game_engine.play()

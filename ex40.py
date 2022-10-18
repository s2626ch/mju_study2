class song(object):
    # 객체 초기화. lyrics 속성에 값
    def __init__(self, lyrics):
        self.lyrics = lyrics


    def sing(self):
        for oneline in self.lyrics:
            print(oneline)

happybirthday = song(["생일 축하합니다", "고소당하기 싫으니까", "여기서 그만"])

bulls_on_parade = song(["조개 껍질 한가득 차고", "가장을 위한다지."])

happybirthday.sing()
bulls_on_parade.sing()

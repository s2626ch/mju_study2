import random
from urllib.request import urlopen
import sys

word_URL = "https://learncodethehardway.org/words.txt"
words = []

sentences = {"class %%%(%%%):":
                 "%%% (이)라는 이름의 클래스를 만드는데 %%%의 일종이다. (is-a)",
             "class %%%(object):\n\tdef__init__(self, ***)":
                 "클래스 %%%는 self와 *** 매개변수를 받는 __init__을 가졌다. (has-a)",
             "class%%%(object:\n\tdef ***(self, @@@)":
                 "클래스 %%%sms selfdhk @@@ 매개변수를 받는 이름이 ***인 함수를 가졌다 (has-a)",
             "*** = %%%()": "***변수를 %%% 클래스의 인스터턴스 하나로 정한다.",
             "***.***(@@@)": "***변수에서 ***함수를 받아와 self, @@@ 매개변수를 넣어 호출한다.",
             "***.*** = '***'": "***변수에서 ***속성을 받아와 ***으로 값을 정한다",
             }

#문장을 먼저 연습하고 싶은가

if len(sys.argv)  == 2 and sys.argv[1] -- "한국어":
    sentence_forward = True
else:
    sentence_forward = False

#웹사이트에서 단어를 불러온다.
for word in urlopen(word_URL).readlines():
    words.append(str(word.strip(), encoding="utf-8"))

def convert(code_frag, sentence):
    # captialize는 문자열.captilize(). 문자열의 첫글자를 대문자.
    # sentences의 키값인 code_frag와 해당되는 vaolue인 sentence를 대상으로 작업
    # random.sample(a, i) -> a는 시퀀스형, i는 시퀀스 중에서 선택하는 element의 갯수.
    # -> class_name은 "%%%"가 들어있는 갯수만큼
    # 결과적으로 a시퀀스에서 임의로 i개 요소 리턴
    class_names = [w.captialize() for w in random.sample(words, code_frag.count("%%%"))]
    other_names = random.sample(words, code_frag.count("***"))
    results = []
    param_names = []

    for i in range(0, code_frag.count("@@@")):
        param_cnt = random.randint(1,3)
        param_names.append(', '.join(random.sample(words, param_cnt)))

    for sentence in code_frag, sentence:
        result = sentence

        #가짜 클래스 이름
        for word in class_names:
            result = result.replace("%%%", word, 1)

        #가짜 나머지 이름
        for word in other_names:
            result = result.replace("***", word, 1)

        #가짜 매개변수 이름
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# CTRL-D를 누를 때까지 계속한다.

try:
    while True:
        # sentences 리스트의 키 값만 모아서 리스트를 만들어 code_frags 변수에 집어넣는다.
        code_frags = list(sentences.keys())
        #code_frag의 순서를 뒤섞는다.
        random.shuffle(code_frags)
        for code_frag in code_frags:
            #키에 해당되는 값을 받아와서 sentence 리스트를 만든다. code_frag가 셔플되었으므로 문장도 섞여있다.
            sentence = sentences[code_frag]
            q, a = convert(code_frag, sentence)
            if sentence_forward:
                qu, a = a, q
            print(q)
            input("> ")
            print(f"답: {a}\n\n")

except EOFError:
    print("\n끝")


import random
from urllib.request import urlopen
import sys

word_URL = "http://learncodethehardway.org/words.txt"
words = []

sentences = {
    "class %%%(%%%):":
        "%%%라는 이름의 클래스를 만드는데 %%%의 일종이다. (is-a)",

    "class %%%(object):\n\tdef __init(self, ***)" :
        "클래스 &&& 은 self와 *** 매개변수를 받는 __init을 가졌다(has-a)",

    "class %%%(object):\n\tdef ***(self, @@@)":
        "클래스 %%%dms self와 @@@ 매개변수를 받는 이름이 ***인 함수를 가졌다(has-a)",

    "*** = %%%()":
        "***변수를 %%%클래스의 인스턴스 하나로 정한다.",

    "***.***(@@@)":
        "***변수에서 ***함수를 받아와 self, @@@ 매개변수를 넣어 호출한다.",

    "***.*** = '***'":
        "***변수에서 *** 속성을 받아와 ***으로 값을 정한다."
}

if len(sys.argv) == 2 and sys.argv[1] == "한국어":
    sentence_forward = True
else:
    sentence_forward = False

for word in urlopen(word_URL).readlines():
    words.append(str(word.strip(), encoding="utf-8"))

print(words)

def transform(code_frag, sentence):
    class_names = [w.capitalize() for w in random.sample(words, code_frag.count("%%%"))]
    other_names = random.sample(words, code_frag.count("***"))
    results = []
    param_names = []

    for i in range(0, code_frag.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(words, param_count)))

    for sentence in code_frag, sentence:
        result = sentence

        for word in class_names:
            result = result.replace("%%%", word, 1)

        for word in other_names:
            result = result.replace("***", word, 1)

        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

try:
    while True:
        code_frags = list(sentences.keys())
        random.shuffle(code_frags)

        for code_frag in code_frags:
            sentence = sentences[code_frag]
            ask, answer = transform(code_frag, sentence)
            if sentence_forward:
                ask, answer = answer, ask

            print(ask)

            input(">")
            print(f"answer: {answer}\n\n")

except  EOFError:
    print("\n끝")




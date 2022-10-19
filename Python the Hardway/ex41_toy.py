import random
import sys


sentence1 = {"1":"a", "2":"b", "3":"c", "4":"e", "5": "f"}
sentence2 = ["1",2,3,4,5]
sentence3 = "abcde"

print('*'*30)
result1 = list(sentence1.values())
print(sentence1)
print("1. 딕셔너리 타입의 값을 list의 매개변수로 받아서 리스트로 출력합니다.")
print(result1)

print('*'*30)
result2 = list(sentence2)
print("2. 리스트의 값을 list의 매개변수로 받아서 리스트로 출력합니다.")
print(result2)

print('*'*30)
print("3. 딕셔너리 타입의 값을 순환하면서 하나씩 꺼내 출력합니다.  ")
for i in result1:
    print(i)

print('*'*30)
w = sentence3.capitalize()
print("4. 문자열을 받아서 첫글자를 대문자로 바꾸어 변수에 넣은 다음 그 변수를 출력합니다. ")
print(w)

print('*'*30)
sentence4 = {"name":"John Smith-", "mobile": "010-2038-1316", "mail": "abc@gmail.com"}
code_frag0 = list(sentence4.values())
result4 = random.shuffle(code_frag0)
print("5. 딕셔너리 형태의 인력 정보입니다.")
print(sentence4)
print("딕셔너리 타입의 키를 받아서 리스트로 만든 결과입니다.")
print("인력정보 값:", code_frag0)
print("딕셔너리 타입의 키를 list의 매개변수로 받아서 random 객체의 sample메소드를 통해 무작위 값 하나를 선택합니다.")
print(result4)

print('*'*30)
print("6. 딕셔너리 형태의 값에서 '-'가 사용된 빈도를 출력합니다.")
sentence5 = "I've been losing you."
print(code_frag0)
sentence6 = code_frag0.pop(0)
print(sentence6)
cnt = sentence6.count('-')
print(cnt)

print('*'*30)
old_sequence = [1,2,3,4,5]
new_sequence = random.sample(old_sequence, 2)
print(new_sequence)

print('*'*30)
new_sequence2 = [w for w in new_sequence]
print(new_sequence2)

print('*'*30)

sentences = {"class %%%(%%%):":
                 "%%% (이)라는 이름의 클래스를 만드는데 %%%의 일종이다. (is-a)",
             "class %%%(object):\n\tdef__init__(self, ***)":
                 "클래스 %%%는 self와 *** 매개변수를 받는 __init__을 가졌다. (has-a)",
             "class%%%(object:\n\tdef ***(self, @@@)":
                 "클래스 %%%sms selfdhk @@@ 매개변수를 받는 이름이 ***인 함수를 가졌다 (has-a)",
             "*** = %%%()": "***변수를 %%% 클래스의 인스터턴스 하나로 정한다.",
             "***.***(@@@)": "***변수에서 ***함수를 받아와 self, @@@ 매개변수를 넣어 호출한다.",
             "***.*** = '***'": "***변수에서 ***속성을 받아와 ***으로 값을 정한다",}
code_frags = list(sentences.keys())
print("첫번째", code_frags)
#code_frag의 순서를 뒤섞는다.
random.shuffle(code_frags)
print("섞인", code_frags)
for code_frag in code_frags:
    sentence = sentences[code_frag]
    print("sentenc: ", sentence)

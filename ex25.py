# -*- coding: utf-8 -*-

import sys

def break_words(stuff):
    """ 문자열을 단어 단위로 쪼개기 """
    words = stuff.split(' ')
    return words

def sort_words(words):
    """ 단어를 정렬 """
    # 내장함수 sorted -> 모든 itterater를 정렬한다. sort()-> 리스트만 정렬
    return sorted(words)

def print_first_word(words):
    """ 첫 단어를 꺼내어 출력"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """ 마지막 단어를 꺼내어 출력"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """ 문자열을 통채로 받아 단어로 쪼개고 쪼갠 단위를 정렬하여 반환"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """ 문장을 받아서 단어로 쪼개고  처음과 마지막 단어를 반환"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

#문장을 받아서 단어로 쪼개고 정렬한 다음 처음과 마지막 단어를 반환
def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

sentence = "All good things come to those who wait."

words = break_words(sentence)
print("단어 분할결과: ", words)
sorted_words = sort_words(words)
print("단어 정렬결과:", sorted_words)
print_first_word(sorted_words)
print_last_word(sorted_words)
print_first_and_last(sentence)
print_first_and_last_sorted(sentence)


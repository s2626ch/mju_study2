# -*- coding: utf-8 -*-

import sys

script, input_encoding, error = sys.argv

def main(lang_file, enconding, errors):
    line = lang_file.readline()

    if line:
        line_out(line, enconding, errors)
        return main(lang_file, enconding, errors)


def line_out(line, encoding, errors):
    next_lang = line.strip()
    raw_bite = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bite.decode(encoding, errors=errors)
    print(raw_bite, "<========>", cooked_string)

langs = open("language.txt", encoding="utf-8")

main(langs, input_encoding, error)
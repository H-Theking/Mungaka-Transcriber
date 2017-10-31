import ToneMap
import os

bottom_diacritics = [u'\u0324', u'\u032F', u'\u0320'] # |̤ |̯ |̠ |
top_diacritics = [u'\u0300', u'\u0301', u'\u0302', u'\u0304', u'\u030C', u'\u030D']



def convert_text():
    file = "sample.txt"
    output_file = open("converted_" + os.path.basename(file), "w", encoding="utf8")
    character_map = ToneMap.map
    with open(file, "r", encoding="utf8") as input_file:
        text = input_file.read(4096)
        output_text = ""
        while len(text):
            diacritics = ''
            previous_letter = text[0]
            for i in range(1, len(text)):
                if text[i] in top_diacritics or text[i] in bottom_diacritics:
                    diacritics += text[i]
                    continue
                combined = previous_letter + diacritics

                try:
                    output_text += character_map[combined]
                except KeyError:
                    output_text += combined
                diacritics = ''
                previous_letter = text[i]
            output_file.write(output_text)
            text = input_file.read(4096)


def is_bottom_diacritic(char):
    return char in bottom_diacritics


def is_top_diacritic(char):
    return char in top_diacritics

convert_text()

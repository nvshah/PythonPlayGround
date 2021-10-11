import re

from functools import partial

def replace_words(text, words, replace_with=""):
    words_s = '|'.join(words)
    regex = r"(?:\s+|\b)(?:{0})(?:\s+|\b)".format(words_s)

    return re.sub(regex, replace_with, text, 0)

remove_words = partial(replace_words, replace_with= ' ')


t = "My Name is Nipun Shah Nipun 106"

tn = remove_words(t, ['106', "is"])

print(tn)


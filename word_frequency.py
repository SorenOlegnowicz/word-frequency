import re


with open('sample.txt') as sample:
    new_text = sample.read()

def word_frequency(new_text):
    edict = {}
    regex_text = re.sub(r'[^A-Za-z\s]', "", new_text).lower().split()
    for word in regex_text:
        if word in edict:
            edict[word] += 1
        else:
            edict[word] = 1
    return edict

print(word_frequency(new_text))

def max_dict(a_dict):
    t_list = sorted(list(edict.items()), key=lambda x: x[1], reverse=True)
    return a[:20]

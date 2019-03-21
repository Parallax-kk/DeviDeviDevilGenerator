# -*- coding: Shift-JIS -*-
from janome.tokenizer import Tokenizer
import json

sjis = open('Data/AromaYogensho.txt', 'rb').read()
text = sjis.decode('Shift-JIS')

t = Tokenizer()
words = t.tokenize(text)

def make_dic(words):
    tmp = ["@"]
    dic = {}
    for i in words:
        word = i.surface
        if word == "" or word == "\r\n" or word == "\n": continue
        tmp.append(word)
        if len(tmp) < 3: continue
        if len(tmp) > 3: tmp = tmp[1:]
        set_word3(dic, tmp)
        if word == ".":
            tmp = ["@"]
            continue
    return dic

def set_word3(dic, s3):
    w1, w2, w3 = s3
    if not w1 in dic: dic[w1] = {}
    if not w2 in dic[w1]: dic[w1][w2] = {}
    if not w3 in dic[w1][w2]: dic[w1][w2][w3] = 0
    dic[w1][w2][w3] += 1

dic = make_dic(words)
json.dump(dic, open("markov-blog.json", "w", encoding="Shift-JIS"))

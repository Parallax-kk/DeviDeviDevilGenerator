# -*- coding: utf-8 -*-
import json
dic = open("markov-blog.json" , "r")
dic = json.load(dic)

tweets_list = []
import random
def word_choice(sel):
    keys = sel.keys()
    ran = random.choice(list(keys))
    return ran

def make_sentence(dic):
    ret = []
    if not "@" in dic: return "no dic"
    top = dic["@"]
    w1 = word_choice(top)
    w2 = word_choice(top[w1])
    ret.append(w1)
    ret.append(w2)
    while True:
        w3 = word_choice(dic[w1][w2])
        ret.append(w3)
        if w3 == "。" or  w3 == ".": break
        w1, w2 = w2, w3
    tweets_list.append(ret)
    return "".join(ret)

for i in range(10):
    s = make_sentence(dic)
    print(s)
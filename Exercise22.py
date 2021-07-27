#Coder: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Phone: 0987773061
#Blog for self-study: https://duythanhcse.wordpress.com
#Facebook for solving coding problem: https://www.facebook.com/groups/communityuni

import random

class Vocabulary:
    def __init__(self,wdict):
        self.words=wdict.copy()
        self.untrained=set(self.words)
        self.renew()

    def renew(self):
        self.target=list(self.untrained)
        random.shuffle(self.target)
        self.untrained=set() #empty set

    def target_keys(self):
        return self.target

    def check(self,key, value=None):
        if key not in self.words:
            return  None
        if value is not None:
            if self.words[key] ==value:
                return Ellipsis
            self.untrained.add(key)
        return self.words[key]

    def shuffle(self):
        random.shuffle(self.target)

wdict ={} #empty dictionary
while True:
    line =input("Spelling and meaning of words to register/memorize:")
    tokens=line.split()
    if len(tokens) !=2:
        break
    wdict[tokens[1]] =tokens[0]

voc=Vocabulary(wdict)
while len(voc.target_keys())>0:
    print("\nwords to memorize:",voc.target_keys())
    nQNA=int(input("Number of questions and answers per word:"))
    print()
    for index in range(0,nQNA):
        voc.shuffle()
        for meaning in voc.target_keys():
            answer=input("What word means '"+meaning+"'?")
            word=voc.check(meaning,answer)
            if word is Ellipsis:
                print("is the correct answer")
            else:
                print("The correct answer is'"+word+"'")
    voc.renew()
print("\nWord learning is over")
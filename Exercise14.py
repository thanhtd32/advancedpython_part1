#Coder: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Phone: 0987773061
#Blog for self-study: https://duythanhcse.wordpress.com
#Facebook for solving coding problem: https://www.facebook.com/groups/communityuni
def frequency(toiecScores):
    counters=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for toiecScore in toiecScores:
        counters[toiecScore//100]+=1
    return counters

def max_frequency(counters):
    max=0
    scoreBase=0
    N=len(counters)
    for i in range(N):
        if max<counters[i]:
            max=counters[i]
            scoreBase=i * 100
    return scoreBase,max

def min_frequency(counters):
    scoreBase=0
    N = len(counters)
    min=11
    for i in range(N):
        if counters[i] !=0 and min >counters[i]:
            scoreBase = i * 100
            min = counters[i]
    return  scoreBase, min

toiecScores=[510,630,750,780,620,805,930,650,840,670]

counters =frequency(toiecScores)
scoreBase,maxCount=max_frequency(counters)

print("#Most score band=%d, frequency=%d" % (scoreBase,maxCount))

scoreBase,minCount=min_frequency(counters)

print("#Least score=%d, frequency=%d" %(scoreBase,minCount))
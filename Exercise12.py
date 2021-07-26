#Coder: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Phone: 0987773061
#Blog for self-study: https://duythanhcse.wordpress.com
#Facebook for solving coding problem: https://www.facebook.com/groups/communityuni

def patternmatch(pattern, correctAns, wrongAns):

    for i in range(len(pattern)-1):
        print(pattern[i],end=" ")

    guessAns=int(input("What's the next number?"))

    if guessAns == pattern[len((pattern))-1]:
        correctAns = correctAns +1
        print("Well done. Congratulations")
    else:
        wrongAns=wrongAns + 1
        print("The correct answer is %d" %(pattern[len((pattern))-1]))
    return  correctAns,wrongAns

correctAns=0
wrongAns=0
#Various number patterns
pattern1=[2, 4, 6, 8]
pattern2=[13, 16, 19, 22]
pattern3=[2, 3, 5, 7, 11]
pattern4=[1, 1, 2, 3, 5, 8]
pattern5=[31, 28, 31, 30]

correctAns,wrongAns=patternmatch(pattern1, correctAns, wrongAns)
correctAns,wrongAns=patternmatch(pattern2, correctAns, wrongAns)
correctAns,wrongAns=patternmatch(pattern3, correctAns, wrongAns)
correctAns,wrongAns=patternmatch(pattern4, correctAns, wrongAns)
correctAns,wrongAns=patternmatch(pattern5, correctAns, wrongAns)

print("%d patterns, %d were correct "%(correctAns+wrongAns,correctAns))


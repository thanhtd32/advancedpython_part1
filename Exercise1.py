#Coder: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Phone: 0987773061
#Blog for self-study: https://duythanhcse.wordpress.com
#Facebook for solving coding problem: https://www.facebook.com/groups/communityuni
print("Please tell me the drink you ordered.")
noA=int(input("Number of Americano (cups):"))
noL=int(input("Number of cafe lattes (cups):"))
noC=int(input("Number of cappuccinos (cups):"))

sum = 0
sum += noA*2500
sum += noL*3000
sum += noC*3000

print("The total amount is:",sum," money ")

money=int(input("Enter the amount to be paid >>"))
if money <sum:
    print("Not enough money.")
else:
    print("Change is",money-sum," money ")


#Coder: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Phone: 0987773061
#Blog for self-study: https://duythanhcse.wordpress.com
#Facebook for solving coding problem: https://www.facebook.com/groups/communityuni
value=0
while True:
    print("\nCurrent value:",value)
    line=input("Enter the work command:")
    tokens=line.split()
    if len(tokens)>0:
        operator=tokens[0]
        if len(tokens) ==1:
            if operator =='x':
                break
            print("Wrong work order!!!!")
        elif len(tokens)==2:
            operand=float(tokens[1])
            if operator== '=':
                value=operand
            elif operator=='+':
                value+=operand
            elif operator=='*':
                value*=operand
            elif operator=='/' or operator=='%':
                if operand!=0:
                    if operator=='/':
                        value/=operand
                    else:
                        value%=operand
                else:
                    print("#Illegal operation command (divided by zero)!!)")
            else:
                print("Wrong work order!!")
        else:
            print("Wrong work order!!")
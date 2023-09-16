#Coder: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Phone: 0987773061
#Blog for self-study: https://tranduythanh.com/


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
            print("Wrong work order!!")
        else:
            listOperand=[]#a list to store all operands
            isAllOperandValid=True
            # loop to store all operands into listOperand
            for i in range(1,len(tokens)):
                if tokens[i].isdigit() == False:
                    isAllOperandValid=False
                    break
                operand = float(tokens[i])
                listOperand.append(operand)
            if isAllOperandValid == True:
                if operator== '=':
                    # get the last operand to asign for value
                    value=listOperand[len(listOperand)-1]
                elif operator=='+':
                    # loop and plus all operand into value variable
                    for operand in listOperand:
                        value+=operand;
                elif operator=='-':
                    # loop and minus all operand into value variable
                    for operand in listOperand:
                        value-=operand;
                elif operator=='*':
                    # loop and multiply all operand into value variable
                    for operand in listOperand:
                        value*= operand;
                elif operator=='^':#loop and exponential all operand into value variable
                    for operand in listOperand:
                        value=pow(value,operand)
                elif operator=='/' or operator=='%':
                    checkDividedZore=False
                    for operand in listOperand:  # loop to check diveded by zero
                        if operand==0:
                            checkDividedZore=True
                            break
                    if checkDividedZore==False:
                        if operator=='/':
                            # loop and devide all operand into value variable
                            for operand in listOperand:
                                value /= operand;
                        else:
                            # loop and mod all operand into value variable
                            for operand in listOperand:
                                value %= operand;
                    else:
                        print("Illegal operation command (divided by zero)!!")
                else:
                    print("Operator is not exist![=,+,-,*,/,%,^]")
            else:
                print("Some operand is not valid!")
    else:
        print("Invalid string input format")

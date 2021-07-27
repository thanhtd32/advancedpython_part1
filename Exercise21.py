#Coder: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Phone: 0987773061
#Blog for self-study: https://duythanhcse.wordpress.com
#Facebook for solving coding problem: https://www.facebook.com/groups/communityuni

#Description:
    #These codes I improved from Exercise 20.
    #1. improve add method when item is the same name->update quantity and total
    #2. improve delete method->check quantity is valid or not, return True/False
    #3. improve printitems method -> text align to print
    #4. call Baseket object and test all method of Baset
class Basket:
    def __init__(self,id):
        self.id=id
        self.items=[]
        self.prices=[]
        self.quantity=[]
        self.total=0
        self.noitems=0
    def add(self,item,price,qty):
        #if item is the same name
        if self.items.__contains__(item) ==True:
            position=self.items.index(item)
            totalPrevious=self.prices[position]*self.quantity[position]
            self.prices[position]=price
            #update quantity for item
            self.quantity[position]=qty+self.quantity[position]
            #remove total of previous
            self.total=self.total-totalPrevious
            #update new total
            self.total+=price *self.quantity[position]
        else:
            self.items.append(item)
            self.prices.append(price)
            self.quantity.append(qty)
            self.total +=price *qty
            self.noitems += 1
    #this function use to delete item from basket
    #return True when deleting successful, False is not successful
    def delete(self,item,qty):
        for i in range(self.noitems):
            if item == self.items[i]:
                #make sure the quantity is valid
                if qty>0 and qty<=self.quantity[i]:
                    self.quantity[i]-=qty
                    self.total -=self.prices[i]*qty
                    if self.quantity[i]==0:
                        self.noitems -=1
                        del self.items[i]
                        del self.quantity[i]
                        del self.prices[i]
                    return True
        return False
    #this function to print all product in baset:
    def printitems(self):
        print(self.id,"Shopping cart")
        print(f'{"Item name":<15}{"Price":<10}{"Quanity":<10}{"Total":<10}')
        print("-"*40)
        for i in range(self.noitems):
            print(f'{self.items[i]:<15}{self.prices[i]:<10}{self.quantity[i]:<10}'
                  f'{self.quantity[i]*self.prices[i]:<10}')
        print("-" * 40)
        print("** total = ",self.total, ", noitems= ",self.noitems)
#create a new Basket object
cjBasket =Basket("John")
#call add function
cjBasket.add("banana",5000,2)
#call add function
cjBasket.add("milk",2000,3)
#call add function
cjBasket.add("apple",3000,1)
#call print items function
cjBasket.printitems()
#call add function with the same item (banana already input)
cjBasket.add("banana",5000,3)
#call print items function
cjBasket.printitems()
#call add function with the same item (apple already input)
cjBasket.add("apple",3000,3)
#call print items function
cjBasket.printitems()
#test delete function:
if cjBasket.delete("milk",1)==True:
    print("delete 1 quanlity of milk is successful")
    cjBasket.printitems()
else:
    print("delete 1 quanlity of milk is NOT  successful")
if cjBasket.delete("milk",2)==True:
    print("delete 2 quanlity of milk is successful")
    cjBasket.printitems()
else:
    print("delete 2 quanlity of milk is NOT  successful")

if cjBasket.delete("milk",2)==True:
    print("delete 2 quanlity of milk is successful")
    cjBasket.printitems()
else:
    print("delete 2 quanlity of milk is NOT  successful")

#Coder: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Phone: 0987773061
#Blog for self-study: https://tranduythanh.com


class Basket:
    def __init__(self,id):
        self.id=id
        self.items=[]
        self.prices=[]
        self.quantity=[]
        self.total=0
        self.noitems=0
    def add(self,item,price,qty):
        self.items.append(item)
        self.prices.append(price)
        self.quantity.append(qty)
        self.total +=price *qty
        self.noitems += 1
    def delete(self,item,qty):
        for i in range(self.noitems):
            if item == self.items[i]:
                self.quantity[i]-=qty
                self.total -=self.prices[i]*qty
                if self.quantity[i]==0:
                    self.noitems -=1
                    del self.items[i]
                    del self.quantity[i]
                    del self.prices[i]
                break
    def printitems(self):
        print(self.id,"shopping cart")
        for i in range(self.noitems):
            print(self.items[i],self.prices[i],self.quantity[i])
        print("** total = ",self.total, ", noitems= ",self.noitems)

cjBasket =Basket("Thanh Tran")
jsBasket =Basket("Pham Dieu")
cjBasket.add("banana",5000,2)
cjBasket.add("Milk",3000,1)
jsBasket.add("Ramen",5900,1)
jsBasket.add("Coffee",10000,2)
cjBasket.printitems()
jsBasket.printitems()
cjBasket.delete("Milk",1)
cjBasket.printitems()
jsBasket.delete("Coffee Mix",1)
jsBasket.printitems()

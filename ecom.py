print("\t\t\t\t\t **WELCOME TO ENGINEERS CANTEEN")
cart={}
bill=0
Wallet=0
a=True
while(a):
    x=int(input(("\n1.PIZZA-150/-\n2.BURGER-100/-\n3.CHICKENROLL-60/-\n4.CAKE-150/-\n5.EGG FUFF-30/-1n6.THUMBSUP-20/-\n7.MILK SHAKE-40/-\n8.RED BULL-100/-\n9.PESPI-20/-\n10.WATER BOTTLE -20/-\n11.EXIT-0/\n\nEnterThe Items: ")))
    if x==1:
        cart.update({"PIZZA":150})
        print(" Successfully Added To Your Bill") 
        bill+=150
    elif x==2:
        cart.update({"BURGER":100})
        print(" Successfully Added To Your Bill") 
        bill+=100
    elif x==3:
        cart.update({"CHICKEN ROLL":60})
        print(" Successfully Added To Your Bill") 
        bill+=60
    elif x==4:
        cart.update({"CAKE":150})
        print(" Successfully Added To Your Bill") 
        bill+=150
    elif x==5:
        cart.update({"EGG FUFF":30})
        print(" Successfully Added To Your Bill") 
        bill+=30
        cart.update({"EGG FUFF":30})
        print(" Successfully Added To Your Bill") 
        bill+=30
    elif x==6:
        cart.update({"THUMBS UP":20})
        print(" Successfully Added To Your Bill") 
        bill+=20
    elif x==7:
        cart.update({"MILK SHAKE":40})
        print(" Successfully Added To Your Bill") 
        bill+=40
    elif x==8:
        cart.update({"RED BULL":100})
        print(" Successfully Added To Your Bill") 
        bill+=100
    elif x==9:
        cart.update({"PESPI":20})
        print(" Successfully Added To Your Bill") 
        bill+=20
    elif x==10:
        cart.update({"WATER BOTTLE":20})
        print(" Successfully Added To Your Bill") 
        bill+=20
    elif x==11:
        a=False
    else:
        print("Enter correct choice")

for i,j in cart.items():
    print(f"{i} - {j}/-")
print(f"Your Bill Is {bill}/-")
print (f"Your Wallet balance is: {Wallet}/-")
y=int(input(("\n1. Add Amount In Your Wallet \n2.Exit\n\tEnter the choice: "))) 
while(True):
    if y==1:
        z=int(input("Enter The Amount:"))
        if z==bill:
            print("Successfully Added To Your Wallet") 
            print("Successfully Payment Your Bill")
            for i,j in cart.items():
                print(f" {i} - {j}/-")
                print(f"Your Bill Is: {bill}/-") 
                print("Thank You Visiting Again.....") 
                break
        elif z>bill:
            print(f"Extra Amount Is {z-bill}/-") 
        elif z<bill:
            print(f" {bill-z}/- Is Less")
        elif y==2:
            break
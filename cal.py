a=int(input("enter number ")) 
operation=int(input("1 for add \n 2 for sub \n 3 for multi \n 4 for div \n 5 for mod \n 6 for intdiv \n 7 for expo")) 
b=int(input("enter number ")) 
if(operation==1):
    print(a+b)
elif(operation==2):
    print(a-b)
elif(operation==3):
    print(a*b)
elif(operation==4):
    print(a/b)    
elif(operation==5):
    print(a%b)
elif(operation==6):
    print(a//b)
elif(operation==7):
    print(a**b)
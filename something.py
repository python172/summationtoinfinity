a= int(input("please type a number"))
sum =1
for x in range (a):
    if(a == 0):
        sum = 1
    else:
        sum = sum * (x+1)
if (a >= 0):
    print (sum)
else: 
    print("insert positive number")

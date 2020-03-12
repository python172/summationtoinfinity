##Summation up to infinity
sum1 = 0
sum2 = 0
#define the value of realtive tolerence
RelTol = 1.e-1000
for n in range(1,100001):
    if (n==1):
        sum1 = 1/((n**2)*((n+1)**2) *((n+2)**2))
    elif (n > 1):
        sum2 = sum1 + 1/(((n)**2)*((n+1)**2)*((n+2)**2))
        RelErr = abs(sum2-sum1)/sum1
        if(RelErr <= RelTol):
            break
        else:
            sum1 = sum2

print("Term: ", n,  "Your summation is ", sum2)
##Summation up to infinity
sum1 = 0
sum2 = 0
#define the value of realtive tolerence
RelTol = 1.e-100

for n in range(100001):
    if (n==0):
        sum1 = (1/(2**n))
    elif (n > 0):
        sum2 = sum1 + (1/(2**n))
        RelErr = abs(sum2-sum1)/sum1
        if(RelErr <= RelTol):
            break
        else:
            sum1 = sum2

print("Your summation is ", sum2)
##Summation up to infinity
sum1 = 0
sum2 = 0
#define the value of realtive tolerence
RelTol = 1.e-6 

for n in range(100001):
    if (n==1):
        sum1 = (1/(n**2))
    elif (n > 0):
        sum2 = sum1 + (1/(n**2))
        RelErr = abs(sum2-sum1)/sum1
        if(RelErr <= RelTol):
            break
        else:
            sum1 = sum2

print("Term: ", n,  "Your summation is ", sum2)

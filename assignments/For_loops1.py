for i in range (151):
    print (i)
    
for multiples in range (0,1001,5):
    print(multiples)
    
for int in range (1,101,1):
    if int % 5==0:
        print ("Coding")
    elif int % 10 ==0:
        print ("Coding Dojo")
    else:
        (print(int))

sum = 0
for odd in range(1, 500001, 2): 
    sum += odd
    print("The final sum:", sum)

for positive in range (2018,0,-4):
    print(positive)

lowNum=2
highNum=9
mult=3

for num in range (lowNum,highNum+1,1):
    if num % mult==0:  
        print (num)
zerovalue =int(input("Please enter 0: "))
anynumber =int(input("Please enter any number: "))

count = 0

print ("They're Prime Numbers in the range : ")  
for number in range (zerovalue, anynumber + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)

zerovalue =int(input("Please enter 0: "))
anynumber =int(input("Please enter any number: "))

print ("The Prime Numbers in the range are: ")  
for number in range (zerovalue, anynumber + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  

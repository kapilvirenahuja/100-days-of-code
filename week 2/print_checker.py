def print_checker(number):
    if number > 100:
        print "Enter a number which is less than 100"
        return
    
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print (f"{number} is not a prime number")
                break
        else:
            print (f"{number} is a prime number")
    else:
        print (f"{number} is not a prime number")


n = int(input ("Enter a number: "))
print_checker(number=n)

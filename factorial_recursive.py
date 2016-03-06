# factorial of a number recursively

def factorial(num):
    if num==1:
        return 1
    else:
        fact=num*factorial(num-1)
        return fact
    

print(factorial(5))
    
    

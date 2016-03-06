# recursive python program to find the value of power(m,n)
# example power(2,5)=32

def power(m,n):
    if n==1:
        return m
    else:
        pwr= power(m,n//2)
        if n%2==0:
            return pwr*pwr    
        else:
            return m*pwr*pwr
    
print(power(2,5))

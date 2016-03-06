# Sum of a python list using recursion

l=[2,5,2,6,88,4,6,8,7]

def listsum(lst):
    if len(lst)==1:
        return lst[0]
    else:
        return lst[0]+listsum(lst[1:])

print(listsum(l))
 

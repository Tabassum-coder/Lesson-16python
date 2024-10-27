def cube(n):
    return n*n*n

def div_by_3(n):
    if(n%3==0):
        return cube(n)
    else:
        return False
    
c1=int(input("Enter a number"))
print("Cube of number is ",div_by_3(c1))
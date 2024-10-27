def factorial(num):
    '''This is recursive function to find factorial of number'''

    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)

n1=int(input("Enter a number to find the factorial"))
print(factorial.__doc__)
print("Factorial of {0} is {1} ".format(n1,factorial(n1)))

# FACTORIAL USING RECURSION
def factorial(n):
    if n<2:
        return 1
    else:
        return n * (factorial(n-1))

n= int(input("Enter the number"))
result= factorial(n)
print("Factorial of ",n," is",result)

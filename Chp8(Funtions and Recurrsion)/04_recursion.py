# recursion is same value or pattern coming back again and again


def factorial(n):
    if (n== 1 or n==0):
        return 1
    return n* factorial(n-1)

a=int(input("Enter the value of number: "))
print(f"The factorial of {a} is:", factorial(a))
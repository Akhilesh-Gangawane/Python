n=int(input("Enter the number: "))
product=1
for i in range(1, n+1):
    product = product*i
    i+=1
print(f"The factorial of {n} is {product}")

    
def compare(n1, n2, n3):
    if (n1>n2 and n1>n3):
        print(f"{n1} is great")
    if (n2>n1 and n2>n3):
        print(f"{n2} is great")
    if (n3>n2 and n1<n3):
        print(f"{n3} is great")

a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
c=int(input("Enter the number: "))

compare(a,b,c)
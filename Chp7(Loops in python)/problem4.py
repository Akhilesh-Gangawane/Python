n=int(input("Enter the number: "))
if (n==2):
    print("The number is even prime number")
   
for i in range(2,n):
    if (n%i ==0):
        print(f"The number {n} is not prime")
        break
        
    else:
        print("The number is prime")
        break
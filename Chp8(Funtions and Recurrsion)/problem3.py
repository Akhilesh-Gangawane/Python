def natural_sum(n):
   if (n==0):
        return "invalid input"
       
   return n*(n+1)/2
   
a=int(input("Enter the number: "))
print(f"The sum of natural number {a} is {natural_sum(a)}")
    
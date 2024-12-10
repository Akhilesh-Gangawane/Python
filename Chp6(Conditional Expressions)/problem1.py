num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
num3=int(input("Enter number 3: "))
num4=int(input("Enter number 4: "))

if(num1>num2 and num1>num3 and num1>num4):
    print("first number is greater",num1)
elif(num2>num1 and num2>num3 and num2>num4):
    print("Second number if greater",num2)
elif(num3>num1 and num3>num2 and num3>num4):
    print("Third number if greater",num3)
elif(num4>num1 and num4>num3 and num4>num2):
    print("Forth number if greater",num4)
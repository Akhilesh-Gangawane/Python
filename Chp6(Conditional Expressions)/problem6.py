Grade=int(input("Enter you're grade: "))

if(100>Grade>=90):
    print("Excellent")

elif(90>Grade>=80):
    print("A")

elif(80>Grade>=70):
    print("B")

elif(70>Grade>=60):
    print("C")

elif(60>Grade>=50):
    print("D")

elif(50>Grade>=40):
    print("E")

elif(Grade<40):
    print("Fail")
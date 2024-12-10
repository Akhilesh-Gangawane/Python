class Programmer:
    company="Microsoft"
    def __init__(self, name, salary, pin):
        self.name=name
        self.salary=salary
        self.pin=pin

p=Programmer("Akhilesh", 664854121, 240051)
print(p.name, p.salary, p.pin)
# print(f"you're name is {p.name} and salary is {p.salary} and pincode is {p.pin}") #this is also valid
a=Programmer("Akhu", 645484, 251002)
print(a.name, a.salary, a.pin)
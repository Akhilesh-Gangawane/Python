
# class attribute is standard for everyone
class Employee:
    Lang="Python"
    salary="1200000"
    
    def getinfo(self): #here denoting is self(in this case only) is necessary to locate 
        print(f"The language is {self.Lang} and salary is {self.salary}")
    def greet(self):
        print("Good morning")
        

# while instance attribute is personnal for everyone(just like exception)
akhilesh=Employee()
akhilesh.Lang="Javascript"
akhilesh.greet()
akhilesh.getinfo() 
# Employee.getinfo(akhilesh) this same as akhilesh.getinfo() 
        
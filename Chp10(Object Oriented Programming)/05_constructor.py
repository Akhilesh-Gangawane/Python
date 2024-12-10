class Employee:
    language="Python"
    salary=1200000

    def __init__(self, name, language, salary): #__init__ is dunder method, and it gets automatically called
            self.name=name
            self.language=language
            self.salary=salary
            print("I am creating an object")        

    def getinfo(self):
        print(f"the language is {self.Lang} and the salary is {self.salary}")

    @staticmethod
    def greetings():
        print("Good morning")

# akhilesh=Employee()
# akhilesh.name="akhilesh"
# print(akhilesh.name, akhilesh.Lang, akhilesh.salary)
# akhilesh.getinfo()

akhu=Employee("Akhu", "Javascript", 5600000)
print(akhu.name, akhu.language, akhu.salary)
        
        
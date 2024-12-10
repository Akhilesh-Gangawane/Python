class calculator:
    def __init__(self, n):
        self.n=n
    
    def square(self):
        print(f"The square of {self.n} is {self.n*self.n}")

    def cube(self):
        print(f"The cube of {self.n} is {self.n**3}")

    def sqrt(self):
        print(f"The squareroot of {self.n} is {self.n**1/2}")
        
a=calculator(4)
a.square()
a.cube()
a.sqrt()
        
        
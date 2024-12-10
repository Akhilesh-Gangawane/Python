class Employee: #this is a class(Noun)
    Lang="Python" #this are class attributes(adjective)
    salary=1200000 #this are class attributes(adjective)

#rane is a object, this is necessary without this class is just like a blank form
rane=Employee() #this is a verb
rane.name=input("Enter you're name: ") #object/instance attribute 
print(rane.name,rane.Lang, rane.salary) #is it called as abstraction and Encapsulation

akhilesh=Employee() 
akhilesh.name=input("Enter you're name: ") #object/instance attribute
print(akhilesh.name, akhilesh.Lang, akhilesh.salary) 

# instance attribute take preference over class attribute during assignment and retrieval
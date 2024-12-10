MyDict={
     "Seamless":"Without any hassle", #seamless=key, Without any hassle=Value 'called as'
     "Disturbance":"Any unplasent activity",
      "Marks":68,
      1:5,
      "NewDict":{"Akhilesh":"Smart Boy", 
                 "Gangawane":"Surname",
                 "Time":"Not Defined"}
}


a=MyDict.keys() #Print the key of dictonary
print(list(a))  
b=MyDict.values() #Print the value of dictonary
print(list(b))
c=MyDict.items() #Print the key,value for all contents of dictonary
print(list(c))
print(MyDict)


# DictUpdate={
#     "girls":72
#     }                       -->this is one method
# MyDict.update(DictUpdate)
# print(MyDict)
MyDict.update({
    "girls":72
})                           #-->this is another to update the dictionary,a lso more input can be added or updated
print(MyDict)


print(MyDict.get("Seamless"))
print(MyDict["Seamless"])

#difference between mydict.get and mydict[]
print(MyDict.get("Seamless5")) #-->output is None
print(MyDict["Seamless5"])     #-->output is error syntax



#more methods are available on docs:python.org
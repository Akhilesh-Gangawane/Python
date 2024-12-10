#Dictionary="key":"value"
#Every key has it's own value
#Cannot have keys of same name if it happen then new key will overwrite old key


MyDict={
    "Seamless":"Without any hassle",
    "Disturbance":"Any unplasent activity",
    "Marks":"68",
    1:5
 }

'''Dictionary are orderless'''
'''Here string, Int, Float, bloat, List, Tuples all are allowed'''
'''But the only condition is should be under curly brackets and given comma for next task'''
'''Key can be int and  written as 1:5 '''
print(MyDict["Seamless"])
print(MyDict["Disturbance"])
print(MyDict["Marks"])
print(MyDict[1])

MyDict={
     "Seamless":"Without any hassle", #seamless=key, Without any hassle=Value 'called as'
     "Disturbance":"Any unplasent activity",
      "Marks":"68",
      "NewDict":{"Akhilesh":"Smart Boy", 
                 "Gangawane":"Surname",
                 "Time":"Not Defined"}
}

print(MyDict["Seamless"])
print(MyDict["Disturbance"])
print(MyDict["Marks"])
print(MyDict["NewDict"]["Akhilesh"])  #--> This is the Subset of large set
print(MyDict["NewDict"]["Time"])
print(MyDict["NewDict"]["Gangawane"])

#To change the value of the key
MyDict["Marks"]=[43]
print(MyDict["Marks"])
'''value of key can be changed on later''' #-->mutable

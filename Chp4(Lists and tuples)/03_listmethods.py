L1=[1,5,8,6,7,3,2,4,9]
print(L1)
'''To sort the list you don't have to create a separate programme like sort_L1=L1.sort()
because it will then not identifies the L1 list and None will come as output'''

L1.sort() #-->for sorting list in ascending order
print(L1)
L1.reverse() #-->for sorting list in descending order
print(L1)
L1.append(10) #-->add 10 at last position
'''append means add someting to the last of the document'''
print(L1)
print(type(L1[9]))
L1.insert( 5, 12) #-->add 12 at 5th index
print(L1)
L1.pop(3) #-->This delete the element of index 3
print(L1)
L1.remove(8) #-->This remove the element (here 8) from list
print(L1)

'''Above commands are linked commands they give output in sequence and continuation of previus of previous codes'''
'''Search "List method python docs" for this kind of command'''
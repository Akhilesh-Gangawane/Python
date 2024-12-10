b=set()
b.add(4)
b.add(5)
b.add(6)
print(b)
'''Here if any no. is coming two times then set wont add it up in set'''

# b.add([4, 5, 6]) 
# b.add({7,8,9})
'''List and dictionary wont be in a set as it is mutable and set are immutable or are non hashable'''

'''But you can add tuple it '''
b.add((1,2,3))
print(b)

'''Non hashable data can't added up in set'''
#Length of the sets
print(len(b))

#removal of data
# b.remove(5)
# print(b)
# b.remove((1,2,3))
# print(b)
'''tuple and elements can be eliminated by remove syntax'''
'''If you enter the the value which is not in the set then programme will through error'''

# Pop of set
print(b.pop())

# clearing of the set
print(b.clear())


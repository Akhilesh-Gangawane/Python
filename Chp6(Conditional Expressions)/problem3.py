# "in" function

p1="Make a lot of money"
p2="buy now"
p3="click this"

msg=input("Enter you're message\n")

if((p1 in msg) or (p2 in msg) or (p3 in msg)):
    print("Spam")
else:
    print("Valid message")
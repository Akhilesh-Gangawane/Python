sub1=int(input("Enter you're marks of subject one "))
sub2=int(input("Enter you're marks of subject two "))
sub3=int(input("Enter you're marks of subject three "))
Total_Marks=(sub1+sub2+sub3)*100/300
print("You're total percentage is: ",Total_Marks)

if(sub1>33):
    print("You passed subject 1")
elif(sub1<33):
    print("You failed subject 1")

if(sub2>33):
    print("You passed subject 2")
elif(sub2<33):
    print("You failed subject 2")

if(sub3>33):
    print("You passed subject 3")
elif(sub3<33):
    print("You failed subject 3")

if(Total_Marks>40):
    print("You passed overall")
else:
    print("You failed overall")


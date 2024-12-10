# 'lower' funtion

post=input("Enter the post\n")

if(("Akhilesh".lower() in post.lower()) ): #lower function here convert Akhilesh in lowercase order and here even AKhiLesh this is valid
    print("This post is talking about Akhilesh") 
else:
    print("NOT TALKING ABOUT Akhilesh")
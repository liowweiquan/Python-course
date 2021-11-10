blog_posts = ["The coolest article 1", "", "How do you overcome struggles", "How to make python yout friend"]

for post in blog_posts:
    if post == "":
        continue
    else:
        print(post)

print("------------------") 

myString = "This is a string"

for char in myString:
    print (char)

print("-------------------")

for x in range(0,10):
    print (x)


print("-------------------")

person = {"Name" : "Wei Quan", "Age" : 33, "Gender" : "Male"}

for key in person:
    print (key, ":", person[key] )

         
print("-------------------")

blog_posts = {"python": ["The coolest article 1", "How do you overcome struggles", "How to make python yout friend"], "Javascript": ["High 10", "high 15"]}

for category in blog_posts:
    print ("Posts about", category)

    for post in blog_posts[category]:
        print (post)

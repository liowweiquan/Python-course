f = open("test1.txt", "a")
f.write("\nthis is the added content")

f = open("test1.txt")
print(f.read())

#w "write"
#a "append"
#r "read"
#x "create"

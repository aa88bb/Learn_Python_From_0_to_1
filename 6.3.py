# f = open("h1.txt","w+")
# li = ["hello world\n","this is nyc\n"]
# f.writelines(li)
# f.close()



# f = open("h1.txt","a+")
#
# context = "goodbye"
#
# f.write(context)
# f.close()

# import os
# if os.path.exists("h1副本.txt"):
#     os.remove("h1副本.txt")


import os
li = os.listdir(".")
print(li)
if "hello.txt" in li:
    os.rename("hello.txt","hello1.txt")
elif "hi.txt" in li:
    os.rename("li.txt","hi1.txt")

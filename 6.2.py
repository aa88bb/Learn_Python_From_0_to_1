# content = "hello world."
#
# f = open('hello.txt','w')
#
# f.write(content)
# f.close()


# f = ("hello.txt")
#
# while True:
#     line = f.readline()
#     if line:
#         print(line)
#     else:
#         break
# f.close()

# f = open("hello.txt")
# lines = f.readlines()
# for i in lines:
#     print(i)
# f.close()

f = open("hello.txt")
context = f.read()
print(context)
f.close()

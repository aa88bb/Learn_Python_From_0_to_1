def jisuan(x=1,y=1,operator="+"):
    result = {
        "+":x+y,
        "-":x-y,
        "*":x*y,
        "/":x/y
    }
    return result.get(operator)

print(jisuan(3,4,"-"))

print((lambda x:-x)(-3))
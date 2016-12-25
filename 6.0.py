word = "version"

print(word.center(20))
print(word.center(20,"*"))
print(word.ljust(2))
print(word.rjust(20))
print("%30s"%word)


strs = ["hello ", "world ", "good"]
result = "".join(strs)
print(result)

sentence = "bob said: 1, 2, 3"
print(sentence.split())
print(sentence.split(","))

sen = "hello world"
print(sen.endswith("ld",6,len(sen)))
li = list(sen)
li.reverse()
s ="".join(li)
print(s)

print(sen[::-1])
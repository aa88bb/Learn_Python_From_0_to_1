import copy

dict = {"a":"apple","b":"banana","o":"orange"}

# print(dict)
#
# print(sorted(dict.items(), key=lambda m:m[0]))

d1 = copy.copy(dict)
d2 = copy.deepcopy(dict)

# d1["o"] = "hahaha"
d2["o"] = "ooooooo"

print(dict)
print(d2)
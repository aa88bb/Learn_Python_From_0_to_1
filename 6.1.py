sentence = "this is a apple."
print(sentence.find("a"))

import time,datetime

print(time.strftime("%Y-%m-%d %X", time.localtime()))

t = time.strptime("2016-09-03","%Y-%m-%d")

y,m,d = t[0:3]
print(datetime.datetime(y,m,d))
ope = "+"

x = 1
y = 2

caozuo = {"+":x+y,"-":x-y,"*":x*y}
if ope in caozuo.keys():
    print(caozuo[ope])

nums = [3,9,2,8]
for j in range(len(nums)-1,-1,-1):
    print(nums[j])
    
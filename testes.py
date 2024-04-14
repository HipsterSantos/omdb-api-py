
"""
 Non optmized version
 uses O(n**2)
 """
num1 = [1,2,3,4,384]
num2 = [384,1,394,30,3]
hash = []
# hashed = []
# # intersaction = [  c for index,c in enumerate(hash) if index <= len(num1)-1]
# for c in range(len(num2)):
#     for a in range(len(num1)):
#         if num1[a] == num2[c]:
#             hashed.append(num1[a])


"""
optmized version 
"""

for c in  num2:
    if c in num1:
        hash.append(c)

print(hash)

num = [12]
target = 13
def checkTarget(num,target):
    for c in num:
        for b in range(len(num)):
            if c + num[b] == target: return [c,num[b]]
    return ["Not Found"]
print("val -- ",checkTarget(num,target),"hover".)

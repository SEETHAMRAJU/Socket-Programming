import sys
arr = raw_input()
a = map(int,arr.split())
a.sort()
ans = ""
for x in a:
    ans += str(x)+" "
print ans

import math

inp = open('10.txt','r')
arr = [[i for i in l.strip()] for l in inp]
# print(arr)
# arr = [int(i) for i in arr[0].split(',')]

pos = []

for r in range(len(arr)):
    for c in range(len(arr[r])):
        if arr[r][c] == '#':
            pos.append((r,c))
print(len(pos))

mx = 0
sign = lambda a: (a>0) - (a<0)
def cal(a,b):
    a1,a2 = a
    b1,b2 = b
    sl = 0
    if b2 == a2:
        sl = float('inf')
    elif a1 == b1:
        sl = 0
    else:
        sl = float(b2-a2)/float(b1-a1)
    return (sl, sign(b2-a2), sign(b1-a1))


for i in pos:
    slopes = set()
    for j in pos:
        if i != j:
            slopes.add(cal(i,j))
    ls = len(slopes)
    if ls > mx:
        mx = ls
        print(i)
    # print(ls, slopes)
print(mx)
best = (19,27)
# print(bs)
import operator
slopes = {}
for j in pos:
    if best != j:
        s = math.atan2(- best[1]+j[1], -best[0]+j[0])
        if s not in slopes:
            slopes[s] = []
        slopes[s].append(j)
# print(slopes.items())
ns = sorted(slopes.items(), key=operator.itemgetter(0))[::-1]
print(ns, len(ns))

cnt = 0
while cnt < 200:
    k = ns[cnt%len(ns)][1].pop(0)
    if len(ns[cnt%len(ns)][1]) == 0:
        ns.pop(cnt%len(ns))
    print(k)
    cnt += 1
    if cnt == 200:
        print('end', k)
        break

# best_slope = ns[0]
# for i in pos:
#     s = cal(best,i)
#     if s == best_slope:
#         print(i)


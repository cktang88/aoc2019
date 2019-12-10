import math
import operator

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
cal = lambda a,b: math.atan2(b[1]-a[1], b[0]-a[0])

for i in pos:
    slopes = set()
    for j in pos:
        slopes.add(cal(i,j))
    ls = len(slopes)
    if ls > mx:
        mx = ls
    # print(ls, slopes)
print(mx)
best = (19,27)
# print(bs)

slopes = {}
for j in pos:
    if best != j:
        s = math.atan2(- best[1]+j[1], -best[0]+j[0])
        if s not in slopes:
            slopes[s] = []
        slopes[s].append(j)
# print(slopes.items())
for s in slopes:
    slopes[s] = sorted(slopes[s], key=lambda k: abs(k[0]-best[0])+abs(k[1]-best[1]))
ns = sorted(slopes.items(), key=operator.itemgetter(0))[::-1]
# print(ns, len(ns))

cnt = 0
i = 0
while cnt < 200:
    k = ns[i][1].pop(0)
    if len(ns[i][1]) == 0:
        ns.pop(i)
        i -= 1
    # print(k)
    cnt += 1
    i += 1
    if cnt == 200:
        print('end', k)
        break


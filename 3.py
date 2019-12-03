inp = open('3.txt','r')
a,b = [l.strip().split(',') for l in inp]

K = 13000

MAX_ANS = 5*K # gamble that the answer is smaller than this for massive speedup

c = [[0]*K for i in range(K)]

cross = set()

# print(a,b)d
x,y = K/2, K/2
t = 0
for m in a:
    ox, oy = x,y
    s,d = m[0], int(m[1:])
    if s == 'R':
        x += d
    if s == 'D':
        y -= d
    if s == 'L':
        x -= d
    if s == 'U':
        y += d
    sn = -1 if x < ox else 1
    for i in range(ox,x, sn):
        if i < K and i >= 0 and c[i][oy] == 0:
            c[i][oy] = t
        t += 1
    sn = -1 if y < oy else 1
    for i in range(oy,y, sn):
        if i < K and i >= 0 and c[ox][i] == 0:
            c[ox][i] = t
        t += 1
    # print('a', x,y)
    if t > MAX_ANS:
        break

print(t)
# for r in c:
#     print(r)

x,y = K/2, K/2
t = 0
twos = set()
for m in b:
    ox, oy = x,y
    s,d = m[0], int(m[1:])
    if s == 'R':
        x += d
    if s == 'D':
        y -= d
    if s == 'L':
        x -= d
    if s == 'U':
        y += d
    sn = -1 if x < ox else 1
    for i in range(ox,x, sn):
        if i < K and i >= 0 and c[i][oy] > 0:
            # print('shit',i,y)
            if (i, oy) not in twos:
                c[i][oy] += t # lol
                cross.add((i, oy))
                twos.add((i, oy))
        
        t += 1
    sn = -1 if y < oy else 1
    for i in range(oy,y, sn):
        if i < K and i >= 0 and c[ox][i] > 0:
            # print('shit',i,x)
            if (ox, i) not in twos:
                c[ox][i] += t # lol
                cross.add((ox, i))
                twos.add((ox, i))
        
        t += 1
    # print('B', x,y)
    if t > MAX_ANS:
        break
print(t)
dst = MAX_ANS
for i,j in cross:
    n = c[i][j]
    if n < dst:
        dst = n
        print(i,j,dst)

# print(sorted(cross))




# print(arr)
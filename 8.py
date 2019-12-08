inp = open('8.txt','r')
arr = [l.strip() for l in inp]
s = arr[0]
pos = 0
cnt = len(s)
ln = 25*6
# ln = 4
tot = [2 for i in range(ln)]
for i in range(0, len(s), ln):
    k = s[i:i+ln]
    # print(k)
    # nc = k.count('0')
    # print(nc, cnt)
    # if nc < cnt:
    #     print('LESS', nc, '@', pos)
    #     cnt = nc
    #     pos = i
    for j in range(ln):
        o = int(k[j])
        if tot[j] == 2:
            tot[j] = o


# print('best', pos)
# k = s[pos:pos+ln]
# print(k)
# print(k.count('1')*k.count('2'))
for i in range(len(tot)):
    if tot[i] == 1:
        tot[i] = '%'
    else:
        tot[i] = ' '
for i in range(6):
    print(''.join([str(c) for c in tot[i*25:(i+1)*25]]))
# print("".join([str(c) for c in tot]))
# print(s)
a = 206938
b = 679128

n = 0
for i in range(a, b):
    d = [int(x) for x in str(i)]
    bad = False
    pair = False
    # check non-decrease, pair
    for j in range(5):
        if d[j] > d[j+1]:
            bad = True
            break
        if d[j] == d[j+1]:
            if (j > 0 and d[j-1] == d[j]) or (j < 4 and d[j+2] == d[j]):
                pass
            else:
                pair = True
    if not bad and pair:
        n += 1
print(n)


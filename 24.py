inp = open("1.txt", "r")
# pad
arr = ["." * 7] + ["." + l.strip() + "." for l in inp] + ["." * 7]
arr = [[c for c in s] for s in arr]
# print(arr)
seen = set()
F = "#"


def pprint(a):
    for r in a[1:-1]:
        print("".join(r[1:-1]))
    print("")


lol = 1
while lol:
    narr = [["." for i in range(7)] for q in range(7)]
    key = 0
    for i in range(1, 6):
        for j in range(1, 6):
            # print(i, j)
            cnt = 0
            if arr[i - 1][j] == F:
                cnt += 1
            if arr[i + 1][j] == F:
                cnt += 1
            if arr[i][j + 1] == F:
                cnt += 1
            if arr[i][j - 1] == F:
                cnt += 1

            if arr[i][j] == F:
                if cnt == 1:
                    narr[i][j] = F
                key += 2 ** (i * 5 + j - 6)
            else:
                if cnt == 1 or cnt == 2:
                    narr[i][j] = F
            # print((i * 5 + j - 1), key)

    if key in seen:
        print("seen", key)
        pprint(arr)
        break
    else:
        # print(key)
        seen.add(key)

    # pprint(narr)
    arr = narr

    lol += 1
    if lol % 1000 == 0:
        print(lol)

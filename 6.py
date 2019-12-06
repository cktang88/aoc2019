inp = open('6.txt','r')
arr = [l.strip() for l in inp]
d = {}
for i in arr:
    a,b = i.split(')')
    if a not in d:
        d[a] = []
    d[a].append(b)
# print(d)

# bound = d['COM']
# cnts = {}
# for i in bound:
#     cnts[i] = 1
# while len(bound) > 0:
#     i = bound.pop(0)
#     if i in d:
#         # print(i, d[i])
#         bound.extend(d[i])
#         for j in d[i]:
#             cnts[j] = cnts[i] + 1
# print(sum(cnts.values()), bound)

# create a reversed adjacency list representation stemming from 'YOU'
newd = {}
for k in d:
    for i in d[k]:
        if i not in newd:
            newd[i] = set()
        newd[i].add(k)
for i in newd:
    if i in d:
        newd[i] = newd[i].union(d[i])

# print(newd)

bound = newd['YOU']
cnts = {}
for i in bound:
    cnts[i] = 1
got = False
while len(bound) > 0:
    i = bound.pop()
    # print(i)
    if i in newd:
        arr = newd[i].difference(cnts.keys())
        if 'SAN' in arr:
            print('ans', cnts[i] - 1)
            got = True
            break
        bound = bound.union(arr)
        for j in arr:
            cnts[j] = cnts[i] + 1
        # print(arr)
print('Verified: ', got)


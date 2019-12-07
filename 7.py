import itertools


def program(inputs):

    inp = open('7.txt','r')
    arr = [l.strip() for l in inp]
    arr = [int(i) for i in arr[0].split(',')]
    # arr[1] = 82
    # arr[2] = 98
    # INPUT = 5
    # print(len(arr), arr)
    a = 0

    def f(n, mode):
        if n > len(arr) - 1 or n < 0:
            return n
        return arr[n] if mode == 0 else n


    while a < len(arr):
        u = arr[a] #+ 100000 # fake pad with lead 0's
        de = u % 100
        u //= 100
        c = u % 10
        u //=10
        b = u % 10
        u //=10
        # A = u%10
        # u //=10
        if de == 99:
            return 'halt'
            break

        i,j,k = f(arr[a+1], c), 0,0
        if de != 3 and de != 4:
            j = f(arr[a+2], b)
        if de < 3 or de > 6:
            k = f(arr[a+3], a)
        # print(i,j,k)
        
        if de == 1:
            arr[k] = i + j
            a += 4
        elif de == 2:
            arr[k] = i*j
            a += 4
        elif de == 3:
            arr[arr[a+1]] = inputs.pop(0)
            a += 2
        elif de == 4:
            print('out: ', i)
            return i
            a += 2
        elif de == 5:
            if i != 0:
                a = j
            else:
                a += 3
        elif de == 6:
            if i == 0:
                a = j
            else:
                a += 3
        elif de == 7:
            arr[k] = (1 if i < j else 0)
            a += 4
        elif de == 8:
            arr[k] = (1 if i == j else 0)
            a += 4
        else:
            print('inv: ', de)
            break
    # print(arr)
    # print(arr[0])

perms = itertools.permutations([5,6,7,8,9])

def engine(perm):
    output = 0
    q = 0
    while output != 'halt':
        output = program([perm[q%5], output])
        q += 1
    print(perm, output)
    return output

ans = []
for perm in perms:
    print(perm)
    ans.append(engine(list(perm)))

print(max(ans))



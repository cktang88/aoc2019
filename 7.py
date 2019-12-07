import itertools

inp = open('7small.txt','r')
arr = [l.strip() for l in inp]
arr = [int(i) for i in arr[0].split(',')]
arrs = [arr for i in range(5)]

def program(inputs, arr, startloc):
    # arr[1] = 82
    # arr[2] = 98
    # INPUT = 5
    print(len(arr), arr)
    a = startloc

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
            return 'halt',a,arr
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
            a += 2
            return i,a,arr
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
    return 'halt',a,arr
    # print(arr)
    # print(arr[0])

perms = itertools.permutations([5,6,7,8,9])
locs = [0,0,0,0,0]
def engine(perm):
    output = 0
    lastout = 0
    q = 0
    while output != 'halt':
        inarr = [perm[q%5], output] if locs[q%5] == 0 else [output]
        print('start with', inarr, locs[q%5])
        output, newloc, newarr = program(inarr, arrs[i], locs[q%5])
        arrs[i] = newarr
        if output != 'halt':
            lastout = output
        locs[q%5] = newloc
        q += 1
        print('endlocs',locs)
        raw_input("cont...")
    print(perm, lastout, locs)
    return lastout

ans = []
for perm in perms:
    print(perm)
    ans.append(engine(list(perm)))

print(max(ans))



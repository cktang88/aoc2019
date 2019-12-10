inp = open('9small.txt','r')
arr = [l.strip() for l in inp]
arr = [int(i) for i in arr[0].split(',')]
# arr[1] = 82
# arr[2] = 98
INPUT = 1
ORIG_LEN = len(arr)
NEW_LEN = 2*ORIG_LEN+100
arr.extend([0]*(NEW_LEN - ORIG_LEN))
print(ORIG_LEN, arr)
a = 0
REL_BASE = 0

def f(n, mode):
    if mode == 0:
        if n > len(arr) - 1 or n < 0:
            print('error: bad input', n, mode)
        return arr[n]
    elif mode == 1:
        return n
    elif mode == 2:
        # if n + REL_BASE > len(arr) - 1 or n + REL_BASE < 0:
        #     print('error: bad input', n, mode)
        return arr[n] + REL_BASE
    else:
        print('bad mode', mode)
        return n


while a < ORIG_LEN:
    u = arr[a] #+ 100000 # fake pad with lead 0's
    de = u % 100
    u //= 100
    c = u % 10
    u //=10
    b = u % 10
    u //=10
    A = u%10
    # u //=10
    if de == 99:
        break

    i,j,k = f(arr[a+1], c), 0,0
    if de != 9:
        if de != 3 and de != 4:
            j = f(arr[a+2], b)
        if de < 3 or de > 6:
            k = f(arr[a+3], A)
    # print(i,j,k)
    
    if de == 1:
        arr[k] = i + j
        a += 4
    elif de == 2:
        arr[k] = i*j
        a += 4
    elif de == 3:
        arr[arr[a+1]] = INPUT
        a += 2
    elif de == 4:
        print('out: ', i)
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
    elif de == 9:
        REL_BASE += arr[a+1]
        a += 2
    else:
        print('inv: ', de)
        break
    # print(arr)
print(arr)
# print(arr[0])

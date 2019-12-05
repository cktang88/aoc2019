inp = open('5.txt','r')
arr = [l.strip() for l in inp]
arr = [int(i) for i in arr[0].split(',')]
# arr[1] = 82
# arr[2] = 98
INPUT = 1
print(len(arr), arr)
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
        break

    i,j,k = f(arr[a+1], c), 0,0
    if de < 3:
        j = f(arr[a+2], b)
        k = arr[a+3] # always writes to position mode
    print(i,j,k)
    
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
    else:
        print('inv: ', de)
        break
    print(arr[:30])
# print(arr)
print(arr[0])

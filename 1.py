inp = open('in.txt','r')
arr = [int(l.strip()) for l in inp]
def f(i):
    res = 0
    while i//3-2 >= 0:
        i = i//3-2
        res += i
    return res
print(f(100756))
print(sum([f(i) for i in arr]))
inp = open('2.txt','r')
arr = [l.strip() for l in inp]
arr = [int(i) for i in arr[0].split(',')]
arr[1] = 82
arr[2] = 98

print(arr)

for a in range(0, len(arr), 4):
    i,j,k = arr[a+1], arr[a+2], arr[a+3]
    if arr[a] == 99:
        break
    elif arr[a] == 1:
        arr[k] = arr[i] + arr[j]
    elif arr[a] == 2:
        arr[k] = arr[i]*arr[j]
    else:
        print('inv')
        break
    # print(a)
print(arr[0])

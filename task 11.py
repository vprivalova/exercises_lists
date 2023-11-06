lst = input().split(' ')
cmmnd = input()

result = []
lngth = len(lst)

if cmmnd[0] == 'R':
    result = lst[lngth - int(cmmnd[1]):] + lst[:lngth - int(cmmnd[1])]
elif cmmnd[0] == 'L':
    result = lst[int(cmmnd[1]):] + lst[:int(cmmnd[1])]

print(result)

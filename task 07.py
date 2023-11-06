numbers = input().split(' ')

even_sum = 0
odd_sum = 0

for elem in numbers:
    if int(elem) % 2 == 0:
        even_sum = even_sum + int(elem)
    else:
        odd_sum = odd_sum + int(elem)

print('Сумма четных:', even_sum)
print('Сумма нечетных:', odd_sum)

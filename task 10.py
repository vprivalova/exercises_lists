lst1 = input().split(' ')
lst2 = input().split(' ')

start_of_rng = int(input())
end_of_rng = int(input())

lst2.extend((lst1[(start_of_rng - 1):end_of_rng])[::-1])
lst1 = lst1[:start_of_rng - 1] + lst1[end_of_rng:]

print('lst1', lst1, 'lst2', lst2)

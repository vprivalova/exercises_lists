numbers1 = input().split(' ')

overall = 0

for elem in numbers1:
    overall = overall + int(elem)

average = overall / len(numbers1)

print(average)

numbers1 = []
numbers2 = []

for index1 in range(10):
    number = int(input())
    numbers1.append(number)

for index2 in range(9):
    numbers2.append(numbers1[index2] + numbers1[index2+1])

print(numbers2)

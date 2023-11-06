number = int(input())

dividers = []

if number > 0:
    for nums in range(1, number + 1):
        if number % nums == 0:
            dividers.append(nums)

elif number < 0:
    for nums in range(number, 0):
        if number % nums == 0:
            dividers.append(nums)

print(dividers)

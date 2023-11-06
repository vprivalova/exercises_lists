SIGNS = '.,?!():"'

sentence = input().split()
result = []

for word in range(len(sentence)):
    for index in range(len(sentence[word])):
        if (sentence[word])[index] in SIGNS:
            sentence[word] = sentence[word].replace((sentence[word])[index], '')

for item in range(len(sentence)):
    sentence[item] = sentence[item].lower()

for elem in sentence:
    if elem not in result:
        result.append(elem)

print(result)

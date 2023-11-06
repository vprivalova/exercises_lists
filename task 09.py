sentence = input()

words = []
SIGNS = '.?!(),:"-/'
decrease = 0
frequency = []

while sentence != '':
    line = sentence.split()

    for word in range(len(line)):
        word = word + decrease

        if line[word] in SIGNS:
            line.pop(word)
            decrease = decrease - 1
        else:
            if (line[word])[0] in SIGNS:
                line[word] = line[word].replace((line[word])[0], '')
            if (line[word])[-1] in SIGNS:
                line[word] = line[word].replace((line[word])[-1], '')

    for item in range(len(line)):
        line[item] = line[item].lower()

    words.extend(line)
    sentence = input()


result = []

for elem1 in words:
    if elem1 not in frequency:
        frequency.append(elem1)

for elem2 in frequency:
    result.append([elem2, words.count(elem2)])

result.sort(key=lambda x: int(x[-1]), reverse=True)

for elem3 in result:
    print(elem3[0])

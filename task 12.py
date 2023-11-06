def letters_checking(line1):
    origin = 'abdegopq'
    with_holes = 0
    without_holes = 0

    line1 = line1.split(' ')

    for word in line1:
        for letter in word:
            if letter in origin:
                with_holes = with_holes + 1
            else:
                without_holes = without_holes + 1

    print('Букв с отверстиями:', with_holes)
    print('Букв без отверстий:', without_holes)


def letters_with_many_holes(line2):
    origin = 'abdegopq'
    list_of_words = []

    line2 = line2.split(' ')

    holes_counter = 0
    for word in line2:
        for letter in word:
            if letter in origin:
                holes_counter = holes_counter + 1

        if holes_counter >= 2:
            list_of_words.append(word)
        holes_counter = 0

    print(list_of_words)


line = input()
letters_checking(line)
letters_with_many_holes(line)

def string_sorting(line):
    symbols = list(line)
    symbols.sort()

    result = ''.join(symbols)

    return result


line1 = input()
print(string_sorting(line1))

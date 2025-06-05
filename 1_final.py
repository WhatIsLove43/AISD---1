NumberDict = {'1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять', '0': 'ноль'}

ReadNumbers = []
BlockSize = 10
AllowedSymbols = '0123456789abcdefABCDEF'
K = 1
NumberSum = 0
NumberMax = 0
CurrentMax = None

while True:
    with open('1_test.txt', 'r') as file:
        for line in file:
            Numbers = line.split()
            for Number in Numbers:
                if Number:
                    if all(Symbol.upper() in AllowedSymbols for Symbol in Number) and (len(Number) > K):
                        Number = int(Number, 16)
                        if (Number % 2 == 0) and (Number <= 2048):
                            ReadNumbers.append(Number)
                            if len(ReadNumbers) == BlockSize:
                                print(ReadNumbers)
                                NumberSum += len(ReadNumbers)
                                ReadNumbers = []

    if ReadNumbers:
        print(ReadNumbers)
        NumberSum += len(ReadNumbers)

        CurrentMax = max(ReadNumbers)
        if CurrentMax > NumberMax:
            NumberMax = CurrentMax

    words = []
    NumberMaxStr = str(NumberMax)
    for i in NumberMaxStr:
        words.append(NumberDict[i])

    print("Количество чисел: ", NumberSum)
    print("Максимальное число: \n", NumberMax)
    print(' '.join(words))



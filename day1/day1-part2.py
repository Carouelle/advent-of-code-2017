# The list is assumed to have en even number of elements
if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        numbersToSum = []
        dataInput = f.read()

        dataSize = len(dataInput)
        step = dataSize / 2

        for i in range(0, dataSize):
            if dataInput[i] == dataInput[(i + step) % dataSize]:
                numbersToSum.append(int(dataInput[i]))
        print sum(numbersToSum)

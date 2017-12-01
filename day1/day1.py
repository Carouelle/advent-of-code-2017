if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        numbersToSum = []
        dataInput = f.read()
        for i in range(0, len(dataInput)):
            if dataInput[i] == dataInput[i + 1 if i + 1 != len(dataInput) else 0]:
                numbersToSum.append(int(dataInput[i]))
        print sum(numbersToSum)

def find_checksum(data):
    running_sum = 0
    for row in data.splitlines():
        largest = 0
        smallest = float("inf")
        for number in row.split('\t'):
            number = int(number)
            if number < smallest:
                smallest = number
            if number > largest:
                largest = number
        running_sum += largest - smallest
    return running_sum


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        print(find_checksum(f.read()))

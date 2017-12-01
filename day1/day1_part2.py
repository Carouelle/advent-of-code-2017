# The list is assumed to have en even number of elements
def find_sum(data):
    data_size = len(data)
    step = int(data_size / 2)
    running_sum = 0
    for i in range(0, len(data)):
        if data[i] == data[(i + step) % data_size]:
            running_sum += int(data[i])
    return running_sum


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        print(find_sum(f.read()))

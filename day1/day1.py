def find_sum(data):
    running_sum = 0
    for i in range(0, len(data)):
        if data[i] == data[(i + 1) % len(data)]:
            running_sum += int(data[i])
    return running_sum


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        print(find_sum(f.read()))

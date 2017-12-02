def find_checksum(data):
    running_sum = 0
    for row in data.splitlines():
        for divider in row.split('\t'):
            divider = int(divider)
            for dividend in row.split('\t'):
                dividend = int(dividend)
                if divider != dividend and divider % dividend == 0:
                    running_sum += divider / dividend
    return running_sum


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        print(find_checksum(f.read()))

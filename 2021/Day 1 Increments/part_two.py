def measure():
    with open('data.txt', 'r') as f:
        lines = f.readlines()
        arr = triple_window_array(lines)
        print(arr)
        print(find_increments(arr))


def triple_window_array(lines) -> [int]:
    triple_measurements = []
    for i in range(0, len(lines) - 2):
        triple_measurements.append(int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2]))
    return triple_measurements


def find_increments(arr):
    counter = 0
    current = arr[0]
    arr.pop(0)
    for value in arr:
        if int(current) < int(value):
            counter += 1
        current = value
    return counter


if __name__ == '__main__':
    measure()

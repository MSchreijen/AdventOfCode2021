def increment():
    with open('data.txt', 'r') as f:
        counter = 0
        lines = f.readlines()

        current = lines[0]
        lines.pop(0)

        for line in lines:
            if int(current) < int(line):
                counter += 1
            current = line

        print(counter)


if __name__ == '__main__':
    increment()

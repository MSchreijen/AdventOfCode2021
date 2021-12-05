def dive():
    with open('data.txt', 'r') as f:
        lines = f.readlines()
        horizontal = 0
        depth = 0
        aim = 0
        for line in lines:
            direction, amount = line.split(' ')
            if direction == 'forward':
                horizontal += int(amount)
                depth += int(amount) * aim
            elif direction == 'down':
                aim += int(amount)
            elif direction == 'up':
                aim -= int(amount)
        print(f'{depth * horizontal = }')


if __name__ == '__main__':
    dive()

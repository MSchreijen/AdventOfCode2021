def dive():
    with open('data.txt', 'r') as f:
        lines = f.readlines()
        horizontal, vertical = 0, 0
        for line in lines:
            direction, amount = line.split(' ')
            if direction == 'forward':
                horizontal += int(amount)
            elif direction == 'down':
                vertical += int(amount)
            else:
                vertical -= int(amount)
        print(f'{horizontal * vertical = }')


if __name__ == '__main__':
    dive()
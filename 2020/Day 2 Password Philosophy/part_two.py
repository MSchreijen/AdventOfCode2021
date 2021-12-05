def verify_password(line: str) -> bool:
    policy, password = [item.strip() for item in line.split(':')]
    bounds = policy.split(' ')[0]
    letter = policy.split(' ')[1]
    first, second = [int(item) for item in bounds.split('-')]

    a = password[first - 1] == letter
    b = (password[second - 1] != letter)
    if (a or b) and (not (a and b)):
        return True
    return False


def count_passwords(data: list):
    good_passwords = 0
    for line in data:
        if verify_password(line):
            good_passwords += 1
    print(f'{good_passwords = }')


if __name__ == '__main__':
    data = []
    with open('data.txt') as f:
        for line in f:
            data.append(line.strip())
    count_passwords(data)

def verify_password(line: str) -> bool:
    policy, password = [item.strip() for item in line.split(':')]
    bounds = policy.split(' ')[0]
    letter = policy.split(' ')[1]
    low, high = [int(item) for item in bounds.split('-')]

    letter_count = password.count(letter)
    if low <= letter_count <= high:
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

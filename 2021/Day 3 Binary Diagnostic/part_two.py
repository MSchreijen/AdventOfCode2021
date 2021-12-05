def scrub():
    with open("data.txt", "r") as f:
        lines = f.readlines()
        binary_oxygen_rating = find_rating(lines, "oxygen")
        binary_co_rating = find_rating(lines, "co")
        oxygen_rating = int(binary_oxygen_rating, 2)
        co_rating = int(binary_co_rating, 2)
        print(f'{oxygen_rating * co_rating = }')


def find_rating(lines: [], mode: str) -> str:
    if mode == "oxygen":
            return most_common(lines, 0)
    else:
        return least_common(lines, 0)


def most_common(lines: [], index: int) -> str:
    if len(lines) == 1:
        return lines[0]
    else:
        filter_char = get_most_common_char(lines, index)
        new_lines = filter_list(lines, index, filter_char)
        return most_common(new_lines, index + 1)


def get_most_common_char(lines: [], index: int) -> chr:
    zero, one = 0, 0
    for line in lines:
        if line[index] == "0":
            zero += 1
        else:
            one += 1
    if one > zero:
        return '1'
    if one == zero:
        return '1'
    else:
        return '0'


def least_common(lines: [], index: int) -> str:
    if len(lines) == 1:
        return lines[0]
    else:
        filter_char = '0' if get_most_common_char(lines, index) == '1' else '1'
        new_lines = filter_list(lines, index, filter_char)
        return least_common(new_lines, index + 1)


def get_least_common_char(lines: [], index: int) -> chr:
    zero, one = 0, 0
    for line in lines:
        if line[index] == "0":
            zero += 1
        else:
            one += 1
    if one > zero:
        return '0'
    if one == zero:
        return '0'
    else:
        return '1'


def filter_list(lines: [], pos: int, char: str) -> [str]:
    newlist = []
    for line in lines:
        if str(line)[pos] == char:
            newlist.append(line)
    return newlist


if __name__ == "__main__":
    scrub()
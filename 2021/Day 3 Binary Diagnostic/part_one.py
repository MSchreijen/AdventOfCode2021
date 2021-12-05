
def binary_dive(lines):
    word_length = len(lines[0]) - 1
    columns = ["" for x in range(word_length)]
    for line in lines:
        for i in range(word_length):
            columns[i] += line[i]
    binary_gamma, binary_epsilon = "", ""
    for column in columns:
        most_occuring, least_occuring = find_most_occuring(column)
        binary_gamma += str(most_occuring)
        binary_epsilon += str(least_occuring)

    gammarate = int(binary_gamma, 2)
    epsilonrate = int(binary_epsilon, 2)

    print(f'{gammarate * epsilonrate = }')


def find_most_occuring(column: str) -> (int,int):
    zero, one = 0, 0
    for char in column:
        if char == '1':
            one += 1
        else:
            zero += 1
    if one > zero:
        return 1, 0
    else:
        return 0, 1


if __name__ == "__main__":
    with open("data.txt", "r") as f:
        binary_dive(f.readlines())
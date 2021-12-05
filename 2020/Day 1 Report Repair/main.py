def main():
    with open('data.txt', 'r') as f:
        lines = f.readlines()
        lines.sort()
        for i in range(0, len(lines) - 1):
            for j in range(len(lines) -1 , 0, -1):
                for k in range(len(lines) -1, 0, -1):
                    if int(lines[i]) + int(lines[j]) + int(lines[k]) == 2020:
                        print(int(lines[i]) * int(lines[j]) * int(lines[k]))


if __name__ == '__main__':
    main()

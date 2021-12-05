def tel_onderdelen():
    with open('data.txt', 'r') as f:
        lines = f.readlines()
        arr = []
        for line in lines:
            name, rawarr = line.split(": ")
            toy = (name, rawarr.split(", "))
            arr.append(toy)
        hoogste: (str, int)
        for toy in arr:
            aantal = tel_aantal(toy, arr)
            if aantal > hoogste[1]:
                hoogste = (toy[0], aantal)


def tel_aantal() -> int:
    return 1


if __name__ == '__main__':
    tel_onderdelen()
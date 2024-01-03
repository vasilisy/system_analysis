from math import log


def task (path):
    with open(path) as csvfile:
        filedata = [[item.rstrip() for item in line.split(",")] for line in csvfile.readlines()]

    H = 0
    n = len(filedata)
    for line in filedata:
        for item in line:
            if item != "0":
                t = float(item)/(n - 1)
                H += t * log(t, 2)
    return (-H)


if __name__ == '__main__':
    path = 'task3.csv'
    print(task(path))

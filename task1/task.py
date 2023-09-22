import csv


def reading_from_csv(path, row, column):
    res = []
    with open(path) as f:
        reader = csv.reader(f)
        for index in reader:
            res.append(index)
    print(res[row][column])


if __name__ == '__main__':
    csv_file_path = 'example.csv'
    row, column = map(int, input().split())
    reading_from_csv(csv_file_path, row, column)

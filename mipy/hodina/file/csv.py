import csv

path = "C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\topeni.txt"
with open(path, "r") as csvfile:
    delimeter = ' '
    reader = csv.reader(csvfile, delimeter)
    for row in reader:
        print(row)


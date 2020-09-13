import csv

with open('grades.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)

    header = next(reader)
    data = [row for row in reader]

    print(header)
    print(data[0])
    # for row in reader:
    #     print(', '.join(row))


# with open('grades.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row.items())
#         # print(row[' "First name"'], row[' "Grade"'])

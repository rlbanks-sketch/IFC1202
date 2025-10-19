import csv

def print_table(table):
    # Determine the width of each column based on the longest item in each column
    col_widths = [max(len(str(row[col])) for row in table) for col in range(len(table[0]))]

    for row in table:
        # Format each row's columns with right alignment for numbers and left for text (city names)
        formatted_row = []
        for i, item in enumerate(row):
            if i == 0 and row != table[0]:  # city name column is left aligned except header row
                formatted_row.append(f"{item:<10}")
            else:
                formatted_row.append(f"{item:>{col_widths[i]}}")
        print(" ".join(formatted_row))


def main():
    filename = "09.Project Distances.csv"

    table = []
    with open(filename, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            table.append(row)

    print_table(table)

    from_city = input("Enter From City: ").strip()
    to_city = input("Enter To City: ").strip()

    # Search the zeroth column for From City (skip header)
    from_index = -1
    for i in range(1, len(table)):
        if table[i][0].strip().lower() == from_city.lower():
            from_index = i
            break

    # Search the zeroth row for To City (skip header)
    to_index = -1
    for j in range(1, len(table[0])):
        if table[0][j].strip().lower() == to_city.lower():
            to_index = j
            break

    if from_index == -1:
        print("Invalid From City")
    elif to_index == -1:
        print("Invalid To City")
    else:
        distance = table[from_index][to_index]
        print(f"{table[from_index][0]} to {table[0][to_index]} - {distance} miles")

if __name__ == "__main__":
    main()

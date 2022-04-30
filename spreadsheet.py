import csv
import sys

# returns a nested list of contents
def read_csv_from_file(filename):
    contents = []
    with open(filename, newline='', encoding='latin-1') as raw_file:
        reader = csv.reader(raw_file)
        next(reader) # skip header line
        for row in reader:
            contents.append(row)
    return contents

if __name__ == "__main__":
    if len(sys.argv) == 2:
        contents = read_csv_from_file(sys.argv[1])
    else:
        print("Needs a spreadhsheet file")
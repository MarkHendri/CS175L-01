#Mark Hendri
#Exception Handling
#Professor Eckert

import sys

def read_data(filename):
    try:
        with open(filename, 'r') as f:
            data = [float(line.strip()) for line in f.readlines()]
        return data
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        sys.exit(1)
    except ValueError:
        print("Error: file contains non-numeric data")
        sys.exit(1)

def calculate_average(data):
    try:
        avg = sum(data) / len(data)
        return avg
    except ZeroDivisionError:
        print("Error: file contains no data")
        sys.exit(1)

def print_average(avg):
    print(f"The average is: {avg:.2f}")

def main():
    filename = input("")

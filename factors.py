#!/usr/bin/python3
import sys

def factorize(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return i, number // i
    return number, 1

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        return

    file_path = sys.argv[1]

    try:
        with open(file_path, 'r') as file:
            for line in file:
                number = int(line.strip())
                factor1, factor2 = factorize(number)
                print(f"{number}={factor1}*{factor2}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except ValueError:
        print("Invalid number in the file.")

if __name__ == '__main__':
    main()

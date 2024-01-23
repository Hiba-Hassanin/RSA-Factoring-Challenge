#!/usr/bin/env python3
import sys
import time


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def factorize_rsa(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            factor1 = i
            factor2 = number // i
            if is_prime(factor1) and is_prime(factor2):
                return factor1, factor2
    return number, 1


def factorize_rsa_number(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                number = int(line.strip())
                factor1, factor2 = factorize_rsa(number)
                print(f"{number}={factor1}*{factor2}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except ValueError:
        print("Invalid number in the file.")


if len(sys.argv) != 2:
    print("Usage: rsa <file>")
    sys.exit(1)

file_path = sys.argv[1]

start_time = time.time()
factorize_rsa_number(file_path)
end_time = time.time()

execution_time = end_time - start_time
print(f"\nExecution time: {execution_time:.3f} seconds")

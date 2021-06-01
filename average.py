#!/usr/bin/env python3

# Created by: Youngjun Kim
# Created on: June 2021
# This program uses an array


import random

def main():
    # this function uses an array

    my_numbers = []
    average = 0

    # input
    for loop_counter in range(0, 10):
        random_number = random.randint(1, 100)
        my_numbers.append(random_number)
        average = average + my_numbers[loop_counter]
        print("The random number is: {0}".format(random_number),
              end="" + "\n")
    print("")

    average = average / 10
    print("The average is {0}".format(average))


if __name__ == "__main__":
    main()

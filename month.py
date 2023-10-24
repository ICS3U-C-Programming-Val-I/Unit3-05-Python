#!/usr/bin/env python3

# Created By: Val Ijaola
# Date: October 23, 2023
# This program asks the user for a number then tells
# them what month is in that place.


def main():
    # Input - get user number
    month_number = int(
        input("Enter a number from 1 to 12 to get the corresponding month\n")
    )
    match month_number:
        case 1:
            print("January")
        case 2:
            print("February")
        case 3:
            print("March")
        case 4:
            print("April")
        case 5:
            print("May")
        case 6:
            print("June")
        case 7:
            print("July")
        case 8:
            print("August")
        case 9:
            print("September")
        case 10:
            print("October")
        case 11:
            print("November")
        case 12:
            print("December")
        case _:
            print("Invalid input. Please enter a number from 1 to 12")


if __name__ == "__main__":
    main()

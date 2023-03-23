# ShippingCharges.py

"""
Author: Austin Miller
Class: CS 170/01
Purpose: Create a function that the returns the shipping charge based on input from main()
"""


def shippingCost(weight, distance):
    shippingRate, blocks, charge = 0, 0, 0
    RATE1, RATE2, RATE3, RATE4 = 1.20, 2.20, 3.80, 4.80
    W1, W2, W3, DIS = 2.0, 6.0, 10.0, 200

    if weight <= W1:
        shippingRate = RATE1
    elif W1 < weight <= W2:
        shippingRate = RATE2
    elif W2 < weight <= W3:
        shippingRate = RATE3
    else:
        shippingRate = RATE4

    blocks = distance // 200
    if distance % 200 > 0:
        blocks += 1

    charge = blocks * shippingRate

    print("Invoice Summary:\n")
    print("\tThe shipping rate is $", format(shippingRate, "0.2f"), "per 200-mile.")
    print("\tThere are", blocks, "200-mile blocks.")
    print("\tThe shipping charge is:", blocks, "x $", shippingRate, "= $", charge)





def main():
    weight = 0
    distance = 0
    weight = eval(input("Enter the weight of the package between 0-50 exclusive: "))
    while weight < 1 or weight > 49:
        weight = eval(input("Weight must be between 0-50 exclusive. Enter the weight: "))
    distance = eval(input("\nEnter the shipping distance between 10-3000 inclusive: "))
    while distance < 10 or distance > 3000:
        distance = eval(input("Sorry, we do not ship less than ten or greater than 3000 miles. Enter a new distance: "))
    print("")
    shippingCost(weight, distance)


main()

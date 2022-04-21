# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math


def square_areas_difference(r):
    radius = r
    diameterAR = 0
    bigSquareAR = (radius * 2) * (radius * 2)
    circleAR = math.pi * (radius * radius)
    littlesquare =0
    littlesqure_lenght = 0
    dia = radius * 2
    lenght = math.sqrt((dia * dia) /2 )
    littlesquare = lenght * lenght
    print("little square rounded " + str(round(littlesquare, 0)))
    print(" little squre cast " + (int(littlesquare)).__str__())
    print("big square is " + bigSquareAR.__str__())
    print(" likttle squre is " +  littlesquare.__str__())
    print("answer is " + (bigSquareAR - int(round(littlesquare, 0))).__str__())

    return bigSquareAR - int(round(littlesquare, 0))

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    square_areas_difference(6)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

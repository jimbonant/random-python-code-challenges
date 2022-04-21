# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def minmax(ar):
    min = 1000000000000
    max = 0
    for a in ar:
        if a < min:
            min = a
        if a > max:
            max = a

    print("min is " + str(min) + " max is " + str(max))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr =[88888,1]

    minmax(arr)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

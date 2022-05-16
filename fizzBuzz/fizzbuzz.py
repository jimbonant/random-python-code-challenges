#fizz buzz

def fizz_buzz(num):
    try:
        num = int(num)
        if num % 3 == 0 and num % 5 == 0:
            return "fizz buzz"
        elif (num % 5) == 0:
            return "buzz"
        elif (num % 3 ) == 0:
            return "fizz"


    except Exception:
        print("there was a problem")


if __name__ == '__main__':
    try:
        while True:
            print(fizz_buzz(input("Write a number")))
           # b = set(range(100))
           # for a in b:
           #    print(fizz_buzz(a))
    except Exception:
        print("totally had an issue , probably user input")

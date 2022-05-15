# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
vs = ['a','e','i','o','u']

def replace_vowles(phrase):
    for i,a in enumerate(phrase) :
        if a in vs:
            phrase[i] = 'e'
    return ''.join(phrase)

def scottish(phrase):
    try:
        phrase = phrase.lower()
        phrase = list(phrase)

        for  a in vs:
            if a in phrase:
                return replace_vowles(phrase)

    except ValueError:
        print("There was an error")

if __name__ == '__main__':
    while True:
       print(scottish(input("enter a sentence")))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

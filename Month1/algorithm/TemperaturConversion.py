from util.Utility import celsius_to_fahrenheit, fahrenheit_to_celsius


def main():
    c = int(input("Enter fahrenheit for converting into celsius : "))
    print(celsius_to_fahrenheit(c))
    f = int(input("Enter celsius for converting into fahrenheit : "))
    print(fahrenheit_to_celsius(f))


if __name__ == '__main__':
    main()

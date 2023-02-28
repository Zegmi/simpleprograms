number = input("enter the number")

try:
    if int(number) % 2 == 0:
        print("even")
    else:
        print("odd")
except ValueError:
    print("invalid input")
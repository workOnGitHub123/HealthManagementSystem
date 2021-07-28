import datetime


def getdate():
    return datetime.datetime.now()


def take(K):
    if K == 1:
        c = int(input("enter 1 for exercise and 2 for food"))
        if c == 1:
            value = input("Type here\n")
            with open("Deepika-ex.txt", "a") as s:
                s.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully written")
        elif c == 2:
            value = input("Type here\n")
            with open("Deepika-food.txt", "a") as s:
                s.write(str([str(getdate())]) + ": " + value + "\n")
                print("Successfully written")
    elif K == 2:
        c = int(input("enter 1 for exercise and 2 for food"))
        if c == 1:
            value = input("Type here\n")
            with open("Sheetal-ex.txt", "a") as s:
                s.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully written")
        elif c == 2:
            value = input("Type here\n")
            with open("Sheetal-food.txt", "a") as s:
                s.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully written")
    elif K == 3:
        c = int(input("Enter 1 for exercise and 2 for food"))
        if c == 1:
            value = input("Type here\n")
            with open("Muskan-ex.txt", "a") as s:
                s.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully written")
        elif c == 2:
            value = input("Type here\n")
            with open("Muskan-food.txt", "a") as s:
                s.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully written")
    else:
        print("Please enter valid input (1(Deepika), 2(Sheetal), 3(Muskan)")


def retrieve(K):
    if K == 1:
        c = int(input("Enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("Deepika-ex.txt") as s:
                for i in s:
                    print(i, end="")
        elif c == 2:
            with open("Deepika-food.txt") as s:
                for i in s:
                    print(i, end="")
    elif K == 2:
        c = int(input("Enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("Sheetal-ex.txt") as s:
                for i in s:
                    print(i, end="")
        elif c == 2:
            with open("Sheetal-food.txt") as s:
                for i in s:
                    print(i, end="")
    elif K == 3:
        c = int(input("Enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("Muskan-ex.txt") as s:
                for i in s:
                    print(i, end="")
        elif c == 2:
            with open("Muskan-food.txt") as s:
                for i in s:
                    print(i, end="")
        else:
            print("Please enter valid input (Harry,Rohan,Hammad)")
    print("Health management system: ")


a = int(input("Press 1 for log the value and 2 for retrieve "))

if a == 1:
    b = int(input("Press 1 for Deepika 2 for Sheetal 3 for Muskan "))
    take(b)
else:
    b = int(input("Press 1 for Deepika 2 for Sheetal 3 for Muskan "))
    retrieve(b)

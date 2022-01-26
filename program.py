# Health Management System

def getdate():
    import datetime
    return datetime.datetime.now()


def log(k):
    if k == 1:
        c = int(input("Enter 1 for exercise and 2 for food "))
        if c == 1:
            value = input("Type here\n")
            with open("Prachi-exercise.txt", "a") as op:
                op.write(str(getdate()) + ": " + value + "\n")
            print("Successfully written!")
        elif c == 2:
            value = input("Type here\n")
            with open("Prachi-food.txt", "a") as op:
                op.write(str(getdate()) + ": " + value + "\n")
            print("Successfully written!")
    elif k == 2:
        c = int(input("Enter 1 for exercise and 2 for food "))
        if c == 1:
            value = input("Type here\n")
            with open("Yuvaan-exercise.txt", "a") as op:
                op.write(str(getdate()) + ": " + value + "\n")
            print("Successfully written!")
        elif c == 2:
            value = input("Type here\n")
            with open("Yuvaan-food.txt", "a") as op:
                op.write(str(getdate()) + ": " + value + "\n")
            print("Successfully written!")
    elif k == 3:
        c = int(input("Enter 1 for exercise and 2 for food"))
        if c == 1:
            value = input("Type here\n")
            with open("Pratik-exercise.txt", "a") as op:
                op.write(str(getdate()) + ": " + value + "\n")
            print("Successfully written!")
        elif c == 2:
            value = input("Type here\n")
            with open("Pratik-food.txt", "a") as op:
                op.write(str(getdate()) + ": " + value + "\n")
            print("Successfully written!")
    else:
        print("Please enter valid input (1(Prachi),2(Yuvaan),3(Pratik)")


def retrieve(k):
    if k == 1:
        c = int(input("Enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("Prachi-exercise.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("Prachi-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 2:
        c = int(input("Enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("Yuvaan-exercise.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("Yuvaan-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 3:
        c = int(input("Enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("Pratik-exercise.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("Pratik-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("Please enter valid input (1(Prachi),2(Yuvaan),3(Pratik)) ")


print("Health Management System: ")
a = int(input("Press 1 to log the value and 2 to retrieve the value "))

if a == 1:
    b = int(input("Press 1 for Prachi, 2 for Yuvaan, 3 for Pratik "))
    log(b)
elif a == 2:
    b = int(input("Press 1 for Prachi, 2 for Yuvaan, 3 for Pratik "))
    retrieve(b)
else:
    print("Please enter valid input (Press 1 to log the value and 2 to retrieve the value)")

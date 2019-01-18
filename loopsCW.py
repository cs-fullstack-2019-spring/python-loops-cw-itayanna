


def main():
    exercise1()
    exercise2()
    exercise3()
    exercise4()
    fizBuzz()



# Print -20 to and including 50. Use any loop you want

def exercise1():
    for x in range(-20, 51):
        print(x)


# Create a loop that prints even numbers from 0 to and including 20

def exercise2():
    for y in range(0, 21):
        print(y)

# Prompt the user for 3 numbers. Then print the 3 numbers along with their average after the 3rd number is entered

def exercise3():
    num1 = int(input("enter a number: "))
    num2 = int(input("eneter another number: "))
    num3 = int(input("enter one more: "))
    average = int((num1 + num2 + num3) / 3)
    print("The average of", num1, ",", num2, "and", num3, "is", average)


# Ask the user to enter a password. Ask them to confirm the password. If it's not equal, keep asking until it's correct or they enter 'Q' to quit.

def exercise4():
    pswd = input("enter your password")
    pswd2 = input("confim your password")
    while pswd != pswd2:
        if pswd2 != "q":
            print("Passwords don't match")
            pswd2 = input("confirm password")
        else:
            break

# classic fiBuz challenge

def fizBuzz():
    userInput= int(input("enter an ending number")+str(1))
    for x in range(1,userInput):
        if x%3==0:
            print("FIZZ")
        elif x%5==0:
            print("BUZZ")
        else:
            print(x)


if __name__ == '__main__':
    main()

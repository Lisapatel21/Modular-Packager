import datetime
import math
import random
import string
import uuid
import sys


# ---------------- DATETIME MENU ----------------

def datetime_menu():
    while True:
        print("\n----- Datetime and Time Operations -----")
        print("1. Current Date and Time")
        print("2. Difference Between Two Dates")
        print("3. Format Current Date")
        print("4. Stopwatch")
        print("5. Countdown")
        print("6. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            now = datetime.datetime.now()
            print("Current Date and Time:", now)

        elif choice == "2":
            date1 = input("Enter first date (YYYY-MM-DD): ")
            date2 = input("Enter second date (YYYY-MM-DD): ")

            try:
                d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
                d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")

                difference = abs((d2 - d1).days)

                print("Difference:", difference, "days")

            except ValueError:
                print("Please enter date in correct format.")

        elif choice == "3":
            today = datetime.datetime.now()
            formatted = today.strftime("%A, %B %d, %Y")
            print("Formatted Date:", formatted)

        elif choice == "4":
            print("Stopwatch Started...")
            input("Press Enter to stop.")

            print("Stopwatch stopped.")

        elif choice == "5":
            import time

            seconds = int(input("Enter seconds: "))

            while seconds > 0:
                print(seconds)
                time.sleep(1)
                seconds = seconds - 1

            print("Time's Up!")

        elif choice == "6":
            break

        else:
            print("Invalid choice.")


# ---------------- MATH MENU ----------------

def math_menu():
    while True:
        print("\n----- Mathematical Operations -----")
        print("1. Factorial")
        print("2. Compound Interest")
        print("3. Trigonometric Calculation")
        print("4. Area of Circle")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            number = int(input("Enter a number: "))

            if number >= 0:
                answer = math.factorial(number)
                print("Factorial:", answer)
            else:
                print("Factorial is not possible for negative numbers.")

        elif choice == "2":
            principal = float(input("Enter principal amount: "))
            rate = float(input("Enter rate of interest: "))
            time = float(input("Enter time in years: "))

            amount = principal * (1 + rate / 100) ** time
            compound_interest = amount - principal

            print("Compound Interest:", round(compound_interest, 2))

        elif choice == "3":
            angle = float(input("Enter angle in degrees: "))

            radians = math.radians(angle)

            print("Sin:", round(math.sin(radians), 4))
            print("Cos:", round(math.cos(radians), 4))
            print("Tan:", round(math.tan(radians), 4))

        elif choice == "4":
            radius = float(input("Enter radius: "))

            area = math.pi * radius * radius

            print("Area of Circle:", round(area, 2))

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


# ---------------- RANDOM MENU ----------------

def random_menu():
    while True:
        print("\n----- Random Data Generation -----")
        print("1. Random Number")
        print("2. Random List")
        print("3. Random Password")
        print("4. Random OTP")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            number = random.randint(1, 100)
            print("Random Number:", number)

        elif choice == "2":
            numbers = []

            for i in range(5):
                number = random.randint(1, 50)
                numbers.append(number)

            print("Random List:", numbers)

        elif choice == "3":
            length = int(input("Enter password length: "))

            characters = string.ascii_letters + string.digits

            password = ""

            for i in range(length):
                password = password + random.choice(characters)

            print("Generated Password:", password)

        elif choice == "4":
            otp = random.randint(100000, 999999)

            print("Your OTP is:", otp)

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


# ---------------- UUID MENU ----------------

def uuid_menu():
    print("\n----- Unique ID Generator -----")

    unique_id = uuid.uuid4()

    print("Generated UUID:")
    print(unique_id)


# ---------------- FILE OPERATIONS ----------------

def file_menu():
    while True:
        print("\n----- File Operations -----")
        print("1. Create File")
        print("2. Write File")
        print("3. Read File")
        print("4. Append File")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            filename = input("Enter file name: ")

            file = open(filename, "w")
            file.close()

            print("File created successfully.")

        elif choice == "2":
            filename = input("Enter file name: ")
            text = input("Enter text: ")

            file = open(filename, "w")
            file.write(text)
            file.close()

            print("Data written successfully.")

        elif choice == "3":
            filename = input("Enter file name: ")

            try:
                file = open(filename, "r")

                data = file.read()

                print("\nFile Content:")
                print(data)

                file.close()

            except FileNotFoundError:
                print("File not found.")

        elif choice == "4":
            filename = input("Enter file name: ")
            text = input("Enter text to append: ")

            file = open(filename, "a")
            file.write("\n" + text)
            file.close()

            print("Data appended successfully.")

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


# ---------------- MODULE EXPLORER ----------------

def explore_module():
    print("\n----- Explore Module -----")

    print("1. math")
    print("2. datetime")
    print("3. random")
    print("4. string")
    print("5. uuid")

    choice = input("Choose module: ")

    if choice == "1":
        print("\nSome math module attributes:")
        print(dir(math)[:15])

    elif choice == "2":
        print("\nSome datetime module attributes:")
        print(dir(datetime)[:15])

    elif choice == "3":
        print("\nSome random module attributes:")
        print(dir(random)[:15])

    elif choice == "4":
        print("\nSome string module attributes:")
        print(dir(string)[:15])

    elif choice == "5":
        print("\nSome uuid module attributes:")
        print(dir(uuid)[:15])

    else:
        print("Invalid choice.")


# ---------------- MAIN PROGRAM ----------------

def main():
    while True:

        print("\n========================================")
        print("       MULTI-UTILITY TOOLKIT")
        print("========================================")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate UUID")
        print("5. File Operations")
        print("6. Explore Module Attributes")
        print("7. Exit")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_menu()

        elif choice == "2":
            math_menu()

        elif choice == "3":
            random_menu()

        elif choice == "4":
            uuid_menu()

        elif choice == "5":
            file_menu()

        elif choice == "6":
            explore_module()

        elif choice == "7":
            print("\nThank you for using Multi-Utility Toolkit!")
            print("Program ended.")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()
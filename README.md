[README (7).md](https://github.com/user-attachments/files/31221958/README.7.md)
# Multi-Utility Toolkit – Modular & Package-Based Python Project

A simple, menu-driven Python program that combines several everyday utilities — date/time tools, math operations, random data generators, a UUID generator, file handling, and a module explorer — into one console application.

This project was built to practice **modular programming** in Python, where each feature is written as its own function and connected together through a main menu.

---

## Project Overview

The **Multi-Utility Toolkit** is a beginner-level Python console project. Instead of writing everything inside one long script, the program is broken down into separate functions — one for each category of operations (datetime, math, random, file handling, etc.). This makes the code easier to read, test, and maintain.

The user interacts with the program through a simple text-based menu and sub-menus, entering numbers to choose the operation they want to perform.

---

## Features

### 1. Datetime and Time Operations

Handled using Python's built-in `datetime` module.

* **Current Date and Time** – Displays the current system date and time.
* **Difference Between Two Dates** – Takes two dates as input and calculates the number of days between them.
* **Format Current Date** – Displays today's date in a readable format (e.g., `Wednesday, August 19, 2026`).
* **Stopwatch** – A simple start/stop interaction using `input()` to pause the program.
* **Countdown** – Counts down from a number of seconds entered by the user, printing each second.

### 2. Mathematical Operations

Handled using Python's built-in `math` module.

* **Factorial** – Calculates the factorial of a non-negative number.
* **Compound Interest** – Calculates compound interest based on principal, rate, and time.
* **Trigonometric Calculation** – Calculates sine, cosine, and tangent of an angle entered in degrees.
* **Area of Circle** – Calculates the area of a circle from a given radius.

### 3. Random Data Generation

Handled using Python's built-in `random` and `string` modules.

* **Random Number** – Generates a random number between 1 and 100.
* **Random List** – Generates a list of 5 random numbers between 1 and 50.
* **Random Password** – Generates a random password of a length entered by the user, using letters and digits.
* **Random OTP** – Generates a random 6-digit OTP.

### 4. UUID Generator

Uses Python's built-in `uuid` module to generate and display a unique identifier (UUID version 4) each time the option is selected.

### 5. File Operations

Demonstrates basic Python file handling using file modes `w`, `r`, and `a`.

* **Create File** – Creates a new empty file.
* **Write File** – Writes text into a file (overwrites existing content).
* **Read File** – Reads and displays the contents of a file, with error handling if the file does not exist.
* **Append File** – Adds new text to the end of an existing file.

### 6. Module Explorer

Uses Python's built-in `dir()` function to display some of the attributes and functions available inside a chosen module.

Modules that can be explored:

* `math`
* `datetime`
* `random`
* `string`
* `uuid`

---

## Python Modules Used

| Module     | Purpose                                |
| ---------- | --------------------------------------- |
| `datetime` | Date and time operations                |
| `math`     | Mathematical calculations               |
| `random`   | Random numbers, passwords and OTP       |
| `string`   | Character sets for password generation  |
| `uuid`     | Unique ID generation                    |
| `sys`      | Imported module used in the project     |

All modules used in this project are part of Python's **Standard Library**, so no external installation is required.

---

## Programming Concepts Demonstrated

* **Functions** – Each feature (datetime, math, random, file handling, etc.) is written as a separate function, making the code organized and reusable.
* **Modular Programming** – The program is split into independent, self-contained menu functions instead of one large block of code.
* **Menu-Driven Programming** – The user navigates the program through numbered menu options.
* **`while` Loops** – Used to keep menus running until the user chooses to go back or exit.
* **`if-elif-else` Statements** – Used to decide which operation to run based on user input.
* **User Input** – The `input()` function is used throughout the program to take values from the user.
* **Exception Handling** – `try-except` blocks are used to catch errors such as invalid date formats and missing files.
* **Python Standard Library Modules** – The project relies entirely on built-in modules (`datetime`, `math`, `random`, `string`, `uuid`, `sys`).
* **File Handling** – Demonstrates creating, writing, reading, and appending files using Python's file objects.
* **Random Data Generation** – Shows how to generate random numbers, lists, passwords, and OTPs.
* **UUID Generation** – Shows how to generate a universally unique identifier.
* **`dir()` Function** – Used to inspect and list the attributes of a Python module.
* **`__name__ == "__main__"`** – Ensures the `main()` function runs only when the file is executed directly, not when imported.

---

## Main Menu

When the program runs, the following main menu is displayed:

```text
========================================
       MULTI-UTILITY TOOLKIT
========================================
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate UUID
5. File Operations
6. Explore Module Attributes
7. Exit
========================================
```

Each option leads to its own sub-menu (except option 4, which directly generates a UUID).

---

## How to Run (Windows)

1. Install Python from the [official Python website](https://www.python.org/) if it is not already installed.
2. Save the file `PR.7 MODULAR & PACKAGER.py` on your computer.
3. Open **Command Prompt**.
4. Navigate to the folder containing the file using the `cd` command. Example:

```bash
cd path\to\your\folder
```

5. Run the program using:

```bash
python "PR.7 MODULAR & PACKAGER.py"
```

No external libraries need to be installed — the project only uses Python's standard library.

---

## Example Output

> **Note:** Random numbers, passwords, OTPs, UUIDs, and dates shown below are just examples. Actual values will differ every time the program runs.

### Main Menu

```text
========================================
       MULTI-UTILITY TOOLKIT
========================================
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate UUID
5. File Operations
6. Explore Module Attributes
7. Exit
========================================
Enter your choice: 2
```

### Mathematical Operation (Factorial)

```text
----- Mathematical Operations -----
1. Factorial
2. Compound Interest
3. Trigonometric Calculation
4. Area of Circle
5. Back
Enter your choice: 1
Enter a number: 6
Factorial: 720
```

### Random Data Generation

```text
----- Random Data Generation -----
1. Random Number
2. Random List
3. Random Password
4. Random OTP
5. Back
Enter your choice: 3
Enter password length: 6
Generated Password: mJu4In
```

### UUID Generator

```text
----- Unique ID Generator -----
Generated UUID:
814914fb-ff2d-4aa5-8882-46e93b049eb8
```

### File Operations

```text
----- File Operations -----
1. Create File
2. Write File
3. Read File
4. Append File
5. Back
Enter your choice: 3
Enter file name: project.txt

File Content:
This is project file.
```

### Module Explorer

```text
----- Explore Module -----
1. math
2. datetime
3. random
4. string
5. uuid
Choose module: 1

Some math module attributes:
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb']
```

### Exit

```text
========================================
       MULTI-UTILITY TOOLKIT
========================================
...
Enter your choice: 7

Thank you for using Multi-Utility Toolkit!
Program ended.
```

---

## Error Handling

The project includes basic error handling for the following situations:

* **Invalid Menu Choice** – If the user enters an option that doesn't exist in a menu, the program prints `"Invalid choice."` and shows the menu again.
* **Incorrect Date Format** – When calculating the difference between two dates, if the date is not entered in `YYYY-MM-DD` format, a `try-except` block catches the `ValueError` and prints `"Please enter date in correct format."`
* **File Not Found** – When reading a file that does not exist, a `try-except` block catches the `FileNotFoundError` and prints `"File not found."`
* **Negative Number for Factorial** – If the user enters a negative number for factorial, the program prints `"Factorial is not possible for negative numbers."` instead of raising an error.

No other advanced validation (such as checking for non-numeric input everywhere) is implemented in this version.

---

## Learning Objectives

Through this project, a student can learn:

* How to break down a large program into smaller, manageable **functions**.
* How to use Python's **standard library modules** (`datetime`, `math`, `random`, `string`, `uuid`) instead of writing everything from scratch.
* How **menu-driven navigation** works using loops and conditional statements.
* How basic **file handling** works in Python (creating, reading, writing, and appending files).
* How to generate **random data** such as numbers, passwords, and OTPs.
* How **UUIDs** are generated and why they are useful as unique identifiers.
* How the **`dir()`** function can be used to explore what a module contains.

---

## Advantages

* Beginner-friendly and easy to follow.
* Fully menu-driven with a simple text interface.
* Uses only Python's standard library — no extra installations needed.
* Demonstrates multiple Python concepts in a single, compact project.
* Code is organized into functions, making it easy to understand and modify.

---

## Limitations

* File operations use basic file handling only; there is no advanced file management (like renaming or deleting files).
* The stopwatch feature is a simple start/stop interaction and does not display elapsed time.
* Random password generation uses only letters and digits (no special characters).
* The program runs only in the console; there is no graphical user interface (GUI).
* There is no external database — files are the only form of storage.
* Not every user input is validated (for example, entering text instead of a number in some fields may cause an error).

---

## Future Enhancements

The following are **possible future improvements** and are **not** part of the current project:

* Add better input validation across all menus.
* Add more mathematical operations (e.g., logarithms, permutations, combinations).
* Add more file management features (rename, delete, list files).
* Build a graphical user interface (GUI) using Tkinter or another library.
* Add more customization options for password generation (special characters, uppercase/lowercase toggle).
* Split the project into separate Python modules/packages for each utility category.
* Improve the stopwatch to show elapsed time instead of just start/stop.

---

## Technologies Used

* Python 3
* Python Standard Library
* Command Prompt / Terminal
* GitHub

---

## Author

**Author:** Lisa Patel
**Project:** PR-7 Modular & Packager
**Language:** Python

---

## Conclusion

The **Multi-Utility Toolkit** is a beginner-friendly Python project that brings together several small utilities into one menu-driven program. It demonstrates the value of **modular programming**, practical use of **Python's standard library**, and core programming concepts such as functions, loops, conditionals, exception handling, and file operations — making it a solid learning project for anyone starting out with Python.

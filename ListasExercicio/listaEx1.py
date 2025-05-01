# Read the name and age of a person and print a personalized greeting.


def exec_1():
    print("Ex: Read the name and age of a person and print a personalized greeting.")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print(f"Hello, {name}! You are {age} years old.")


# Create a program that reads two numbers and displays their sum, subtraction, multiplication, and division.


def exec_2():
    print(
        "Ex: Create a program that reads two numbers and displays their sum, subtraction, multiplication, and division."
    )
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"Sum: {num1 + num2}")
    print(f"Subtraction: {num1 - num2}")
    print(f"Multiplication: {num1 * num2}")
    print(f"Division: {num1 / num2 if num2 != 0 else 'undefined (division by zero)'}")


# Ask the user for a number and inform whether it is even or odd.


def exec_3():
    print("Ex: Ask the user for a number and inform whether it is even or odd.")
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")


# Request two numbers and show which one is greater.


def exec_4():
    print("Ex: Request two numbers and show which one is greater.")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num1 > num2:
        print(f"{num1} is greater than {num2}.")
    elif num2 > num1:
        print(f"{num2} is greater than {num1}.")
    else:
        print(f"{num1} and {num2} are equal.")


# Read a number and display its multiplication from 1 to 10.


def exec_5():
    print("Ex: Read a number and display its multiplication from 1 to 10.")
    num1 = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{num1} x {i} = {num1 * i}")


# Read the temperature in Celsius and convert it to Fahrenheit.


def exec_6():
    print("Ex: Read the temperature in Celsius and convert it to Fahrenheit.")
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F.")


# Check if a number is a multiple of both 3 and 5.


def exec_7():
    print("Ex: Check if a number is a multiple of both 3 and 5.")
    num = int(input("Enter a number: "))
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} is a multiple of both 3 and 5.")
    else:
        print(f"{num} is not a multiple of both 3 and 5.")


# Request a person’s weight and height and calculate their IMC.


def exec_8():
    print("Ex: Request a person’s weight and height and calculate their IMC.")
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))
    ## Notem que a fórmula do IMC é peso dividido pela altura ao quadrado.
    ## A fórmula do IMC é: IMC = peso / (altura * altura)
    IMC = weight / (height**2)  ## O IMC foi definido como uma constante.

    print(f"Your IMC is {IMC:.2f}.")


# Check if a year is a leap year.


def exec_9():
    print("Ex: Check if a year is a leap year.")
    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


# Read three numbers and display the largest and the smallest.


def exec_10():
    print("Ex: Read three numbers and display the largest and the smallest.")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    if num1 >= num2 and num1 >= num3:
        largest = num1
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    else:
        largest = num3
    if num1 <= num2 and num1 <= num3:
        smallest = num1
    elif num2 <= num1 and num2 <= num3:
        smallest = num2
    else:
        smallest = num3
    print(f"The largest number is {largest}.")
    print(f"The smallest number is {smallest}.")


# Create a program that reads a password and keeps requesting it until it is correct.


def exec_11():
    print(
        "Ex: Create a program that reads a password and keeps requesting it until it is correct."
    )
    password = "1234"
    input_password = input("Enter the password: ")
    while input_password != password:
        print("Incorrect password. Try again.")
        input_password = input("Enter the password: ")


# Calculate the average of 4 grades, checking if the student passed (average ≥ 7).


def exec_12():
    print(
        "Ex: Calculate the average of 4 grades, checking if the student passed (average ≥ 7)."
    )
    nota1 = float(input("Enter the first grade: "))
    nota2 = float(input("Enter the second grade: "))
    nota3 = float(input("Enter the third grade: "))
    nota4 = float(input("Enter the fourth grade: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    if media >= 7:
        print(f"Passed with an average of {media:.2f}.")
    else:
        print(f"Failed with an average of {media:.2f}.")


# Read a number n and calculate the sum from 1 to n.


def exec_13():
    print("Ex: Read a number n and calculate the sum from 1 to n.")
    n = int(input("Enter a number: "))
    soma = sum(range(1, n + 1))
    print(f"The sum from 1 to {n} is {soma}.")


# Count how many even numbers exist between two input numbers.


def exec_14():
    print("Ex: Count how many even numbers exist between two input numbers.")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    count = 0
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            count += 1
    print(f"There are {count} even numbers between {num1} and {num2}.")


# Generate the first 10 numbers of an arithmetic progression with common difference r and initial term a1.


def exec_15():
    print(
        "Ex: Generate the first 10 numbers of an arithmetic progression with common difference r and initial term a1."
    )
    num1 = int(input("Enter the first term (a1): "))
    num2 = int(input("Enter the common difference (r): "))
    for i in range(10):
        print(num1 + i * num2, end=" ")


def main():
    exec_1()
    exec_2()
    exec_3()
    exec_4()
    exec_5()
    exec_6()
    exec_7()
    exec_8()
    exec_9()
    exec_10()
    exec_11()
    exec_12()
    exec_13()
    exec_14()
    exec_15()


if __name__ == "__main__":
    main()

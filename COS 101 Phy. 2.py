
# COS 101 ASSIGNMENT
# FIVE PHYSICS FORMULAS
# Functions, While Loop and Input Validation


# FUNCTION TO GET VALID NUMBERS
def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a number and try again.\n")


# FUNCTION TO GET VALID FORMULA SELECTION
def get_choice():
    while True:
        choice = input("Choose a physics operation (1-5): ")

        if choice in ["1", "2", "3", "4", "5"]:
            return choice
        else:
            print("Invalid selection! Please choose a number between 1 and 5.\n")


# 1. SPEED = DISTANCE / TIME
def calculate_speed():
    distance = get_number("Enter distance (m): ")

    while True:
        time = get_number("Enter time (s): ")

        if time != 0:
            break

        print("Time cannot be zero. Please try again.\n")

    speed = distance / time
    print("Speed =", speed, "m/s")


# 2. FORCE = MASS * ACCELERATION
def calculate_force():
    mass = get_number("Enter mass (kg): ")
    acceleration = get_number("Enter acceleration (m/s^2): ")

    force = mass * acceleration
    print("Force =", force, "N")


# 3. DENSITY = MASS / VOLUME
def calculate_density():
    mass = get_number("Enter mass (kg): ")

    while True:
        volume = get_number("Enter volume (m^3): ")

        if volume != 0:
            break

        print("Volume cannot be zero. Please try again.\n")

    density = mass / volume
    print("Density =", density, "kg/m^3")


# 4. WEIGHT = MASS * GRAVITY
def calculate_weight():
    mass = get_number("Enter mass (kg): ")
    gravity = 9.8

    weight = mass * gravity
    print("Weight =", weight, "N")


# 5. WORK DONE = FORCE * DISTANCE
def calculate_work():
    force = get_number("Enter force (N): ")
    distance = get_number("Enter distance (m): ")

    work = force * distance
    print("Work Done =", work, "J")


# MAIN PROGRAM
while True:

    print("\n===== PHYSICS FORMULA CALCULATOR =====")
    print("1. Calculate Speed")
    print("2. Calculate Force")
    print("3. Calculate Density")
    print("4. Calculate Weight")
    print("5. Calculate Work Done")

    choice = get_choice()

    if choice == "1":
        calculate_speed()

    elif choice == "2":
        calculate_force()

    elif choice == "3":
        calculate_density()

    elif choice == "4":
        calculate_weight()

    elif choice == "5":
        calculate_work()

    print("\nWould you like to perform another calculation?")

    while True:
        again = input("Enter yes or no: ").strip().lower()

        if again in ["yes", "no"]:
            break

        print("Invalid response! Please enter yes or no.\n")

    if again == "no":
        print("\nThank you for using the Physics Formula Calculator!")
        break
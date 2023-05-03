import math

# define a function to calculate energy consumption
def calculate_energy_consumption():
    watts = float(input("Enter the watts of the device: "))
    hours = float(input("Enter the hours used: "))
    kwh = (watts * hours) / 1000

    return kwh

# define a function to calculate cost
def calculate_cost(kwh, rate):
    cost = kwh * rate
    return cost

# define a function to suggest energy-saving tips based on consumption
def suggest_energy_saving(kwh):
    if kwh >= 900:
        print("Your monthly energy consumption is bad. It is " + str(kwh) + " kWh.")
        print("Here are some tips to reduce your energy consumption:")
        print("- Take shorter showers")
        print("- Use less electricity")
        print("- Turn off devices when not in use")
    else:
        print("Your energy consumption is good. Keep up the good work! It is " + str(kwh) + " kWh.")

# define a function to get the electricity rate
def get_electricity_rate():
    while True:
        rate = input("Enter your electricity rate in $/kWh (press Enter for default rate of $0.12/kWh): ")
        if not rate:
            rate = 0.12
            break
        try:
            rate = float(rate)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    return rate

# define a function to get user confirmation
def get_user_confirmation():
    while True:
        user_input = input('Do you want to continue? (y/n): ')
        if user_input.lower() == 'y':
            return True
        elif user_input.lower() == 'n':
            return False
        else:
            print('Invalid input. Please enter y or n.')

# main program
print("Welcome to the energy calculator.")

while True:
    # calculate energy consumption
    kwh = calculate_energy_consumption()

    # suggest energy-saving tips
    suggest_energy_saving(kwh)

    # get electricity rate
    rate = get_electricity_rate()

    # calculate cost
    cost = calculate_cost(kwh, rate)

    # display result
    print("Your cost would be $" + str(round(cost, 2)) + ".")

    # ask for user confirmation to continue
    if not get_user_confirmation():
        break

print('Thanks for using this calculator!')

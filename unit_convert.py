def km_to_miles(km):
    return km * 0.621371


def miles_to_km(miles):
    return miles / 0.621371


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def kg_to_pounds(kg):
    return kg * 2.20462


def pounds_to_kg(pounds):
    return pounds / 2.20462


def show_menu():
    print("\nUnit Converter")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Kilograms to Pounds")
    print("6. Pounds to Kilograms")
    print("7. Exit")


def main():
    while True:
        show_menu()
        choice = input("Select an option (1-7): ")

        if choice == "1":
            km = float(input("Enter kilometers: "))
            print(f"{km} km = {km_to_miles(km):.2f} miles")
        elif choice == "2":
            miles = float(input("Enter miles: "))
            print(f"{miles} miles = {miles_to_km(miles):.2f} km")
        elif choice == "3":
            celsius = float(input("Enter Celsius: "))
            print(f"{celsius}°C  = {celsius_to_fahrenheit(celsius):.2f}°F")
        elif choice == "4":
            fahrenheit = float(input("Enter Fahrenheit: "))
            print(f"{fahrenheit}°F  = {fahrenheit_to_celsius(fahrenheit)}°C")
        elif choice == "5":
            kg = float(input("Enter Kilograms: "))
            print(f"{kg} kg = {kg_to_pounds(kg):.2f} lbs")
        elif choice == "6":
            pounds = float(input("Enter Pounds: "))
            print(f"{pounds} lbs = {pounds_to_kg(pounds):.2f} kg")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid Option. Please try again.")


if __name__ == "__main__":
    main()

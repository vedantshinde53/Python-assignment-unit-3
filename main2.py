from temperature import celsius_to_fahrenheit as c2f
from temperature import fahrenheit_to_celsius as f2c
from temperature import celsius_to_kelvin as c2k

def main():
    print("--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    
    choice = input("\nSelect an option (1-3): ")

    if choice == '1':
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C is {c2f.c_to_f(c):.2/f}°F")
    
    elif choice == '2':
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f}°F is {f2c.f_to_c(f):.2/f}°C")
    
    elif choice == '3':
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C is {c2k.c_to_k(c):.2/f}K")
    
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
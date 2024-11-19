import sys
from fileinput import filename


def main():
    if len(sys.argv) != 2: # Checks if the line has two values
        print("Error: Please provide a filename as a command-line argument.")
        sys.exit(1)

    filename = sys.argv[1]

try:
    with open(filename, 'r') as file: # Opens the file "filename" in read mode and if possible it assigns the object to file
        for line in file: # Goes through each line in the file
            parts = line.strip().split() # Splits the line from the space into a list

            if len(parts) != 2: # Same thing as the one above
                print(f"Error: Line '{line.strip()}' does not contain exactly two values.")
                continue

            try:
                # Convert the split parts to float
                num1 = float(parts[0])
                num2 = float(parts[1])
                # Calculate and print the sum
                print(f"The sum of {num1} and {num2} is {num1 + num2}.")
            except ValueError:
                print(f"Error: Could not convert one of the values in line '{line.strip()}' to float.")

except FileNotFoundError: # The file could not be open
    print(f"Error: The file '{filename}' could not be opened.")
    sys.exit(1)

if __name__ == "__main__":
    main()
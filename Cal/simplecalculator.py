class Calculator:
    def __init__(self, value=0):
        self.value = value  # Store result or initial number

    # --- Method Overloading Simulation (variable arguments) ---
    def add(self, *args):
        return sum(args)

    def subtract(self, a, *args):
        result = a
        for num in args:
            result -= num
        return result

    def multiply(self, *args):
        result = 1
        for num in args:
            result *= num
        return result

    def divide(self, a, *args):
        result = a
        for num in args:
            if num != 0:
                result /= num
            else:
                return "Error! Division by zero."
        return result

    # --- Static Methods ---
    @staticmethod
    def square(num):
        return num * num

    @staticmethod
    def cube(num):
        return num ** 3

    # --- Operator Overloading ---
    def __add__(self, other):
        return Calculator(self.value + other.value)

    def __sub__(self, other):
        return Calculator(self.value - other.value)

    def __mul__(self, other):
        return Calculator(self.value * other.value)

    def __truediv__(self, other):
        if other.value != 0:
            return Calculator(self.value / other.value)
        else:
            return "Error! Division by zero."

    def __str__(self):
        return f"Calculator Value: {self.value}"


# --- Example Usage ---
calc = Calculator()

print("Method Overloading Examples:")
print("Add:", calc.add(1, 2, 3, 4))           # 10
print("Subtract:", calc.subtract(10, 2, 3))   # 5
print("Multiply:", calc.multiply(2, 3, 4))    # 24
print("Divide:", calc.divide(100, 2, 5))      # 10.0

print("\nStatic Method Examples:")
print("Square:", Calculator.square(5))        # 25
print("Cube:", Calculator.cube(3))            # 27

print("\nOperator Overloading Examples:")
c1 = Calculator(10)
c2 = Calculator(5)

print(c1 + c2)   # 15
print(c1 - c2)   # 5
print(c1 * c2)   # 50
print(c1 / c2)   # 2.0



class Calculator:
    def __init__(self):
        print("=== Simple OOP Calculator ===")

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error! Division by zero."

    def get_numbers(self):
        """Private helper to take user input for numbers"""
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b

    def run(self):
        """Main loop for calculator"""
        while True:
            print("\nSelect operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Exit")

            choice = input("Enter choice (1/2/3/4/5): ")

            if choice == '5':
                print("Exiting Calculator... Goodbye!")
                break

            if choice in ('1', '2', '3', '4'):
                num1, num2 = self.get_numbers()

                if choice == '1':
                    print(f"Result: {self.add(num1, num2)}")
                elif choice == '2':
                    print(f"Result: {self.subtract(num1, num2)}")
                elif choice == '3':
                    print(f"Result: {self.multiply(num1, num2)}")
                elif choice == '4':
                    print(f"Result: {self.divide(num1, num2)}")
            else:
                print("Invalid input! Please choose 1-5.")


# Create object and start calculator
calc = Calculator()
calc.run()


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error! Division by zero."


# Main program
calc = Calculator()

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(f"Result: {calc.add(num1, num2)}")
elif choice == '2':
    print(f"Result: {calc.subtract(num1, num2)}")
elif choice == '3':
    print(f"Result: {calc.multiply(num1, num2)}")
elif choice == '4':
    print(f"Result: {calc.divide(num1, num2)}")
else:
    print("Invalid input!")

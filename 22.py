names = [ "Alice", "Bob", "Charlie", "David", "Eve" ]

d = {name  : len(name )for name in names }
print(d)


city_population = { "New York" : 8000000, "Los Angeles" : 4000000, "Chicago" : 2700000 }


large_cities = { city : population for city, population in city_population.items() if population > 3000000 }
print(large_cities)
import re
from typing import Union

class Calculator:
    """A strong basic calculator with support for common mathematical operations."""
    
    def __init__(self):
        self.history = []
    
    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        result = a + b
        self._record(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """Subtract two numbers."""
        result = a - b
        self._record(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        result = a * b
        self._record(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: float, b: float) -> float:
        """Divide two numbers with error handling."""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        result = a / b
        self._record(f"{a} / {b} = {result}")
        return result
    
    def power(self, base: float, exponent: float) -> float:
        """Calculate base raised to exponent."""
        result = base ** exponent
        self._record(f"{base} ^ {exponent} = {result}")
        return result
    
    def square_root(self, a: float) -> float:
        """Calculate the square root of a number."""
        if a < 0:
            raise ValueError("Cannot calculate square root of a negative number!")
        result = a ** 0.5
        self._record(f"√{a} = {result}")
        return result
    
    def modulo(self, a: float, b: float) -> float:
        """Calculate remainder of division."""
        if b == 0:
            raise ValueError("Cannot perform modulo with zero!")
        result = a % b
        self._record(f"{a} % {b} = {result}")
        return result
    
    def percentage(self, value: float, percent: float) -> float:
        """Calculate percentage of a value."""
        result = (value * percent) / 100
        self._record(f"{percent}% of {value} = {result}")
        return result
    
    def factorial(self, n: int) -> int:
        """Calculate factorial of a number."""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers!")
        if not isinstance(n, int):
            raise ValueError("Factorial is only defined for integers!")
        
        result = 1
        for i in range(2, n + 1):
            result *= i
        self._record(f"{n}! = {result}")
        return result
    
    def evaluate(self, expression: str) -> float:
        """Safely evaluate a mathematical expression."""
        # Remove spaces
        expression = expression.replace(" ", "")
        
        # Validate expression (only allow numbers, operators, and parentheses)
        if not re.match(r'^[0-9+\-*/.()%^]+$', expression):
            raise ValueError("Invalid characters in expression!")
        
        try:
            # Replace ^ with ** for Python exponentiation
            expression = expression.replace('^', '**')
            result = eval(expression)
            self._record(f"{expression} = {result}")
            return result
        except ZeroDivisionError:
            raise ValueError("Division by zero in expression!")
        except Exception as e:
            raise ValueError(f"Invalid expression: {str(e)}")
    
    def _record(self, operation: str) -> None:
        """Record operation in history."""
        self.history.append(operation)
    
    def get_history(self) -> list:
        """Get calculation history."""
        return self.history
    
    def clear_history(self) -> None:
        """Clear calculation history."""
        self.history = []
    
    def display_history(self) -> None:
        """Display all calculations in history."""
        if not self.history:
            print("No calculation history yet.")
        else:
            print("\n=== Calculation History ===")
            for i, operation in enumerate(self.history, 1):
                print(f"{i}. {operation}")
            print("=" * 26)


class CalculatorApp:
    """Interactive calculator application."""
    
    def __init__(self):
        self.calc = Calculator()
        self.running = True
    
    def display_menu(self) -> None:
        """Display the main menu."""
        print("\n" + "=" * 40)
        print("          STRONG CALCULATOR")
        print("=" * 40)
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Power (^)")
        print("6. Square Root (√)")
        print("7. Modulo (%)")
        print("8. Percentage")
        print("9. Factorial (!)")
        print("10. Evaluate Expression")
        print("11. View History")
        print("12. Clear History")
        print("0. Exit")
        print("=" * 40)
    
    def get_two_numbers(self) -> tuple:
        """Get two numbers from user input."""
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            return a, b
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            return None
    
    def run(self) -> None:
        """Run the calculator application."""
        print("\nWelcome to Strong Calculator!")
        
        while self.running:
            self.display_menu()
            choice = input("\nSelect an operation (0-12): ").strip()
            
            try:
                if choice == '0':
                    print("\nThank you for using Strong Calculator!")
                    self.running = False
                
                elif choice == '1':
                    nums = self.get_two_numbers()
                    if nums:
                        print(f"Result: {self.calc.add(nums[0], nums[1])}\n")
                
                elif choice == '2':
                    nums = self.get_two_numbers()
                    if nums:
                        print(f"Result: {self.calc.subtract(nums[0], nums[1])}\n")
                
                elif choice == '3':
                    nums = self.get_two_numbers()
                    if nums:
                        print(f"Result: {self.calc.multiply(nums[0], nums[1])}\n")
                
                elif choice == '4':
                    nums = self.get_two_numbers()
                    if nums:
                        print(f"Result: {self.calc.divide(nums[0], nums[1])}\n")
                
                elif choice == '5':
                    nums = self.get_two_numbers()
                    if nums:
                        print(f"Result: {self.calc.power(nums[0], nums[1])}\n")
                
                elif choice == '6':
                    try:
                        num = float(input("Enter a number: "))
                        print(f"Result: {self.calc.square_root(num)}\n")
                    except ValueError as e:
                        print(f"Error: {e}\n")
                
                elif choice == '7':
                    nums = self.get_two_numbers()
                    if nums:
                        print(f"Result: {self.calc.modulo(nums[0], nums[1])}\n")
                
                elif choice == '8':
                    try:
                        value = float(input("Enter the value: "))
                        percent = float(input("Enter the percentage: "))
                        print(f"Result: {self.calc.percentage(value, percent)}\n")
                    except ValueError:
                        print("Invalid input!\n")
                
                elif choice == '9':
                    try:
                        num = int(input("Enter a number: "))
                        print(f"Result: {self.calc.factorial(num)}\n")
                    except ValueError as e:
                        print(f"Error: {e}\n")
                
                elif choice == '10':
                    expression = input("Enter expression (e.g., 5 + 3 * 2): ")
                    try:
                        print(f"Result: {self.calc.evaluate(expression)}\n")
                    except ValueError as e:
                        print(f"Error: {e}\n")
                
                elif choice == '11':
                    self.calc.display_history()
                
                elif choice == '12':
                    self.calc.clear_history()
                    print("History cleared!\n")
                
                else:
                    print("Invalid choice! Please try again.\n")
            
            except Exception as e:
                print(f"An error occurred: {e}\n")


# Run the calculator
if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
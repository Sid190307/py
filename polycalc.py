class Calculator:
    def add(self, a, b, c=0):
        result = a + b + c
        return result

calc = Calculator()

# Input for two numbers
print("Addition of Two Numbers")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = calc.add(a, b)
print("Result:", result)

# Input for three numbers
print("\nAddition of Three Numbers")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

result = calc.add(a, b, c)
print("Result:", result)

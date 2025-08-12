#addition of two numbers
def addition(x,y):
    return x+y
#subtraction of two numbers
def subtraction(x,y):
    return x-y
#Multiplication of two numbers
def multiplication(x,y):
    return x*y
#Division of two numbers
def division(x,y):
    return x/y if y != 0 else "Division by zero is not allowed"
print("Welcome to the simple calculator!")
# Input from the user 
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction") 
print("3. Multiplication")
print("4. Division") 
# check the choice of operation          
choice = input("Enter choice (1/2/3/4): ")
num1 = float(input("Enter first number: ")) 
num2 = float(input("Enter second number: "))
if choice == '1':
    print(f"{num1} + {num2} = {addition(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {subtraction(num1, num2)}")               
elif choice == '3':
    print(f"{num1} * {num2} = {multiplication(num1, num2)}")        
elif choice == '4': 
    print(f"{num1} / {num2} = {division(num1, num2)}")
else:
    print("Invalid input! Please enter a valid choice (1/2/3/4).")
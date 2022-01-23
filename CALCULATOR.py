#Calculator

#Add
def add(n1,n2):
  return n1 + n2

#Subtract
def subtract(n1,n2):
  return n1-n2

#Multiply
def multiply(n1,n2):
  return n1*n2

#Division

def divide(n1,n2):
  return n1/n2

#Operations dictionary
operations = {
"+" :add,
"-" : subtract,
"*" : multiply,
"/" : divide,
}




#Create calculator function for recursion
def calculator():

  #importing the logo art

  from art import logo
  from replit import clear

  print(logo)

  #setting condition for while loop

  should_continue= True

#Create variable for input number 1
  num1 = float(input("What's the first number?: "))

#Loop through the dictionary operations
  for key in operations:
   print(key)

#Selecting the operations

  operation_symbol = input("Pick an operation from the line above: ")

#Create a variable for number 2
  num2 = float(input("What's the second number?: "))

#First stage of the calculations
  calculation_function = operations[operation_symbol]
  answer = calculation_function(num1,num2)

  print(f"{num1} {operation_symbol} {num2} = {answer}")

#For the next calculations
  while should_continue:
   choice = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation or any other key to exit\n ").lower()

   if choice == 'y':
    saved_answer = answer
    operation_symbol = input("Pick another operation: ")
    num3 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(saved_answer,num3)
    print(f"{saved_answer} {operation_symbol} {num3} = {answer}")

   elif choice == 'n':
    should_continue = False
    clear()
    calculator()
  
   else:
    print("Goodbye")
    exit()

  

calculator()
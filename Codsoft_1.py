import math

def add(x,y):
  return x + y

def sub(x,y):
  return x - y

def mul(x,y):
  return x * y

def div(x,y):
  if y == 0:
    return "Error!Division by zero"
  else:
    return x/y
  
def exp(x,y):
  return x ** y

def sqrt(x):
  if x < 0 :
    return "Error! Can't find out square root of negative number."
  else:
    return math.sqrt(x)

def mod(x,y):
  if y == 0:
    return  "Error! can't do modulus of zero"
  else:
    return x%y
  
def fldiv(x,y):
  if y == 0:
    return "Error! Can't divide by zero."
  else:
    return x//y
  
def calculator():
    print("Welcome to calculator : ")
    print("Choose Operation : ")
    print("1. add")
    print("2. sub")
    print("3. mul")
    print("4. div")
    print("5. exp")
    print("6. sqrt")
    print("7. mod")
    print("8. fldiv")
    
    while True:
      try:
        choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")
        
        if choice in ['1','2','3','4','5','7','8']:
          num1 = float(input("Enter first number: "))
          num2 = float(input("Enter second number: "))
          if choice == '1':
            print(f'{num1} + {num2} : {add(num1,num2)}')
          elif choice == '2':
            print(f'{num1} - {num2} : {sub(num1,num2)}')
          elif choice == '3':
            print(f'{num1} * {num2} : {mul(num1,num2)}')
          elif choice == '4':
            print(f'{num1}/{num2} : {div(num1,num2)}')
          elif choice == '5':
            print(f'{num1} ** {num2} : {exp(num1,num2)}')
          elif choice == '7':
            print(f'{num1} % {num2} : {mod(num1,num2)}')
          elif choice == '8':
            print(f'{num1} // {num2} : {fldiv(num1,num2)}')
        elif choice == '6':
          num1 = float(input("Enter number: "))
          print(f"{num1} : {sqrt(num1)}")
        else:
            print("Invalid input!Please enter a valid operator")
            
        next_calculation = input("Do you want to do more calculations?(y/n) : ").lower()
        if next_calculation != 'y':
          print("Thank you for using calculator :)")
          break
      except ValueError:
        print("Input Invalid!Enter valid number")
        
calculator()


            

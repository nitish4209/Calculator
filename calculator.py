# Creating a calculator using Python

def Add(num1,num2):
    return num1 + num2

def Sub(num1,num2):
    return num1 - num2

def Mul(num1,num2):
    return num1 * num2

def Div(num1,num2):
    if num2 == 0:
        return "Error: Cannot divide by zero"
    return num1 / num2

def Avg(num1,num2):
    return (num1 + num2)/2

print("Please select the option:\n" \
    "1. Addition\n" \
    "2. Subtraction\n" \
    "3. Multiplication\n"\
    "4. Division\n"\
    "5. Average\n")

select = int(input("Select the operation from (1/2/3/4/5): "))

num1 = float(input("Enter the num1: "))
num2 = float(input("Enter the num2: "))

if select == 1:
    print(num1,"+",num2,"=",Add(num1,num2))
    
elif select == 2:
     print(num1,"-",num2,"=",Sub(num1,num2))

elif select == 3:
     print(num1,"*",num2,"=",Mul(num1,num2))
     
elif select == 4:
     print(num1,"/",num2,"=",Div(num1,num2))
     
elif select == 5:
     print("(",num1,"+",num2,")","/","2","=",Avg(num1,num2))
     
else:
    print("Invalid Input")
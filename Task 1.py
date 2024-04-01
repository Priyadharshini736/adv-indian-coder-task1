def add(num1,num2):#defining addition function
    return num1+num2
def sub(num1,num2):#defining subtraction function
    return num1-num2
def mul(num1,num2):#defining multiplication function
    return num1*num2
def div(num1,num2):#defining division function
    return num1/num2
print("Select the required operation:\n"\
      "1. Addition (+) \n" \
      "2. Subtraction (-) \n" \
      "3. Multiplication (*) \n" \
      "4. Division (\) \n" )
operator = int(input("Select operations form 1,2,3,4:"))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if operator == 1:
    print(num1,"+",num2,"=",add(num1,num2))
elif operator == 2:
    print(num1,"-",num2,"=",sub(num1,num2))
elif operator == 3:
    print(num1,"*",num2,"=",mul(num1,num2))
elif operator == 4:
    print(num1,"/",num2,"=",div(num1,num2))
else:
    print("Please enter a valid arithmetic operation")
                
      

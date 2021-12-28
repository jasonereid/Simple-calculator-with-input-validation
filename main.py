# simple calculator project

print("Welcome to my simple calculator project. \nThis will take your input and perform simple calculations on it. \nPress Q to quit at any time.")

# get the numbers and store as variables
# validate input - numbers only
print("First, choose your first number.")
while True:
    num1=input()
    try:
        num1 = int(num1)
    except:
        print("Please type a number")
        continue
    break

print("Next, choose a second number.")
while True:
    num2=input()
    try:
        num2 = int(num2)
    except:
        print("Please type a number")
        continue
    break

print("Ok, now choose - will you add, subtract, multiply, or divide these numbers? \n Input + for add, - for subtract, * for multiply, and / for divide.")
oper1=input()
# validate input
while (oper1 != ("+" or oper1 == "-" or oper1 == "*" or oper1 == "/")):
    print("Please input a proper math operator.")
    oper1 = input()
    continue

# perform math
if oper1 == "+":
    print(num1+num2)
elif oper1 == "-":
    print(num1-num2)
elif oper1 == "*":
    print(num1*num2)
elif oper1 == "/":
    print(num1/num2)





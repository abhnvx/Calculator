from divide import divide
from multiply import multiply
from add import add
from Subtract import subtract
from power import power

a = int(input("Enter first operand : "))
b = int(input("Enter second operand : "))

print("----------CALCULATOR----------")
print("1.Add[a+b]")
print("2.Subtract[a-b]")
print("3.Multiply[a*b]")
print("4.Divide[a/b]")
print("5.Power[a^b]")

op = int(input("Enter operation [1-5]"))

if op == 1:
    result = add(a,b)
    print("Sum is :", result)

elif op == 2:
    result = subtract(a, b)
    print("Difference is ", result)

elif op == 3:
    result = multiply(a, b)
    print("Answer is ", result)

elif op == 4:
    result = divide(a, b)
    print("Answer is ", result)

elif op == 5:
    result = power(a, b)
    print("Answer is ", result)
    


    

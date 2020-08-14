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

op = int(input("Enter operation [1-6]"))

if op == 1:
    result = add.add(a, b)
    print("Sum is", res)

elif op == 2:
    result = Subtract.subtract(a, b)
    print("Difference is", res)

elif op == 3:
    result = multiply.multiply(a, b)
    print("Answer is", res)

elif op == 4:
    result = divide.divide(a, b)
    print("Answer is", res)

elif op == 5:
    result = power.power(a, b)
    print("Answer is", res)
    


    

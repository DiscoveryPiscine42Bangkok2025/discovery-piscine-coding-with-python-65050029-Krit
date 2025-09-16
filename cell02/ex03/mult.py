num1 = int(input("Input first Number : "))
num2 = int(input("Input second Number : "))
num3 = num1 * num2
MutiNum = num1 * num2

print(num1,'x',num2,'=',num3)
if num1 * num2 < 0:
    print("The result is negative.") 
elif num1 * num2 > 0:
    print("The result is positive.")
else:
    print("The result is positive and negative.")
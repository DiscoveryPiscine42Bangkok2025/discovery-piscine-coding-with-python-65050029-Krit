num1 = int(input("Input first Number : "))
num2 = int(input("Input second Number : "))
multnum = num1 * num2

print(num1,'x',num2,'=',multnum)
if num1 * num2 < 0:
    print("The result is negative.") 
elif num1 * num2 > 0:
    print("The result is positive.")
else:
    print("The result is positive and negative.")
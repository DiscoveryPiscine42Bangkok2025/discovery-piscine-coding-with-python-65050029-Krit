num1 =int(input("Enter your num: "))
num2 =int(input("Enter your num: "))
print('Thank you!')
add = num1+num2
minus = num1-num2
mult = num1*num2 
if num2 != 0 :
    division = num1//num2 
else:
    print('Cannot divide by zero')
print(num1, "+", num2, "=", add)
print(num1, "-", num2, "=", minus)
print(num1, "/", num2, "=", division)
print(num1, "*", num2, "=", mult)
print("Enter a number less than 25")
num = int(input("Input your number: "))

if num < 25 :
    for num in range(num,26):
        print("Inside the loop, my variable is",num)         
else:
    print("Error")
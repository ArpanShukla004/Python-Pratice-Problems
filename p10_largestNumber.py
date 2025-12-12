num1 = float(input("Enter number 1 :"))
num2 = float(input("Enter number 2 :"))

num3 = float(input("Enter number 3 :"))

if(num1>num2 and num1>num3):
    print(num1 ," num1 is largest")
elif(num2>num1 and num2>num3):
    print(num2, "num2 is largest")
else:
    print(num3,"num3 is largest")
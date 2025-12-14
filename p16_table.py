num = int(input("Enter a number to print its multiplication table: "))
for i in range(1,11):
    print(num, "x", i, "=", num*i)



# method 2 using while loop
num2 = int(input("Enter a number to print its multiplication table using while loop: "))
i = 1
while i <= 10:
    print(num2, "x", i, "=", num2*i)

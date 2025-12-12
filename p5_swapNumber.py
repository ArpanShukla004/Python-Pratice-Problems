# method 1 
num1 = float(input("Enter number 1 :")) # 5
num2 = float(input("Enter number 2 :")) #3

num3 = num1  #num3 = 5
num1 = num2  #num1 = 3
num2 = num3 #num2 = 5

print("The number 1 is :" , num1)
print("The number 2 is :", num2 )

# method 2
num3 = float(input("Enter number 3"))
num4 = float(input("Enter number 4"))
num3,num4 = num4,num3
print("The value of num1 is :" , num3)
print("The value of num2 is", num4)

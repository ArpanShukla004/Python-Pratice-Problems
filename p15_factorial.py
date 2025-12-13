# method 1

# num = int(input("Enter the number :"))

# fact = 1

# if num < 0 :
#     print("factorial does not exist :")
# elif(num == 0):
#     print("Factorial of 0 is 1" , 1)
# else:
#     for i in range(1,num+1):
#         fact = fact * i


# print("the factorail of number is" , fact)


# method 2 

def fact(a):
    if a == 0:
        return 1
    else:
        return ((a) * fact(a-1))
    
num2 = int(input("enter a number 2 :"))

result = fact(num2)
print("The result of facorial is ", result)
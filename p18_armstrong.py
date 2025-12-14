# arm strong number ----  cube of digits of number gives the number itself


num = int(input("Enter a number here :"))

order = len(str(num))

sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    cube = digit ** order
    sum = sum + cube
    temp = temp // 10

if num == sum:
    print(num , "is an armstrong number")
else:
    print(num , "is not an armstrong number")
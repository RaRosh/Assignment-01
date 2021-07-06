

num = input ("Enter a number: ")
int_num = int(num)

check = input ("Enter a number: ")
int_check = int(check)

num2 = int_num % int_check
int_num2 = int(num2)


if (int_num2 == 0):
    print( "check divides num evenly")
else:
    print("check does not divide num evenly")

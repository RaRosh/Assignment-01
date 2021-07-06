num = input ("Enter a number: ")
if num.isdigit():
    num = int(num)
    num1 = num % 2
    num2 = num % 4

    if (num1 == 0):
        print("The entered number is Even")
        print("The remainder is %s ", num1)

        if (num2 == 0):
            print("The entered number is divisible by 4")
            print("The remainder is %s ", num2)
    else:
        print("The entered number is Odd")

else:
    print("The entered number is invalid")


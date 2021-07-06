
age = input ("Enter your Age:")

if age.isdigit():
    int_age = int(age)
    yrs_req = 100 - int_age
    yrs_100 = 2021 + yrs_req
    print("You will turn 100 in the year %s", yrs_100)

else:
    print("Please enter a valid age")
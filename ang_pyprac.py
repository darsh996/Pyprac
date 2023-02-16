# Data Conversion

# two_num = input("Enter two digits:" )
# print(type(two_num))
# n1 = int(two_num[0])
# n2 = int(two_num[1])
# sum = n1+n2
# # sum = int(two_num[0])+int(two_num[1])
# print("Addtion is:",sum)

# --------------------------------------------
# Mathematical Operation
# PEMDAS--> Parenthesis,Exponent,Multiplication,Division,Addition,Subtraction

# BMI Calculator

# Formula = weight/sq. of height

# print("BMI Calculator")
# he = float(input("Enter your height(m):"))
# we = float(input("Enter your weight(kg):"))
# bmi = we /(he**2)
# print("Your BMI is:",round(bmi))

# --------------------------------------------

# f-string

# isWinnig = True
# Score = 1
# Player = "Ram"
# print(f"Team A has scored {Score} through {Player} and are they winnig {isWinnig}")

# --------------------------------------------

# Exercise
# To find how many days,weeks and months are left in my life to be 90

# current_age = int(input("Whats your age:"))
# years_left = 90 - current_age
# days_left = 365 * years_left
# weeks_left = int(days_left/7)
# months_left = int(years_left*12)
# print(f"You have {years_left} years, {days_left} days, {weeks_left} weeks and {months_left} months left to be 90.")

# --------------------------------------------

# Tip calculator
    
# print("Welcome to tip calculator")
# total_bill = float(input("Your total bill:"))
# tip_per = int(input("What percentage tip would ypu like to give 10,12,or 15:"))
# split = int(input("How many people to split the bill:"))

# tip = (tip_per/100) * total_bill
# total = (total_bill+tip)/split
# r_total = round(total, 2)
# r_total = "{:.2f}".format(total)
# print("Each person will pay: $",r_total)

# --------------------------------------------

print("Welcome to Pizza Corner!!!!")
print("Small Pizza  :$15")
print("Medium Pizza :$20")
print("Large Pizza  :$25")

size = input("Press S,M,L :")
quan = input("Please select quantity:")

if size == "S":
    ex_pep = input("Would you like Pepperoni extra $2 per pizza(Y/N):")
    if ex_pep == "Y":
        total = 17
    else:
        total = 15
if size == "M":
    ex_pep = input("Would you like pepperoni extra $3 per pizza(Y/N):")
    if ex_pep == "Y":
        total = 23
    else:
        total = 20
if size == "L":
    ex_pep = input("Would you like pepperoni extra $3 per pizza(Y/N):")
    if ex_pep == "Y":
        total = 28
    else:
        total = 25

ex_ch = input("Would you like extra cheese for $3 per pizza(Y/N):")
if ex_ch == "Y":
    total += 3
    
gr_total = total*quan

print("*****Your Order Summary*****")
print("size           :",size)
print("Quantity       :",quan)
print("Extra Pepporini:",ex_pep)
print("Extra Cheese   :",ex_ch)  
print("Total          :",gr_total)
    


















# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

num = int(input("Give number to find divisors:"))
x = []
n = 0
for n in range(0,num):
    n = n+1
    if num % n ==0:
        x.append(n)
print(x)


num = int(input("Give me number:"))
x = []
n = 0
while (n < num):
    n = n+1
    if num % n == 0:
        x.append(n)
print(x)

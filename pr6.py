# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

name = str(input("Enter name to check palindrome:")).lower()

revstr = ""
for n in name:
    revstr = n + revstr
print("Reverse name is:",revstr)

if revstr == name:
    print("String is palindrome")
else:
    print("Not palindrome")       
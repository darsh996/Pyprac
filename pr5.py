# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 2]
b = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 2, 2]
x = []
for n in a:
    if n in b and n not in x:
        x.append(n)
print(x)
# Write a program to print all the positive numbers from the list.

list_1 = [12, -7, 5, 64, -14]
list_2 = [12, 14, -95, 3]

for num in list_1:

    if num >= 0:
        print(num, end=", ")

print("\n")

for num in list_2:
    if num > 0:
        print(num, end=", ")

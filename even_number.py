# coding:utf-8
"""The proposal of the exercice is to define whether the number is even or odd"""

X = "X"
print("The proposal of the exercice is to define whether the X is even or uneven.")
while True:
    try:
        X = int(input("Let's have "+ X +" = "))
        break
    except ValueError:
        print(X, "must be an integer ;) Try again...")

if X % 2 == 0:
    print(str(X) + " is an even number")

else:
    print(str(X) + " is an uneven number")

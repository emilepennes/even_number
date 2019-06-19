# coding:utf-8
# The proposal of the exercice is to define whether the number is even or odd

x = "x"

while True :
    try :
        x = int(input("Soit "+ x +" = "))
        break
    except ValueError :
        print(x, "must be an integer ;) Try again...")

if x % 2 == 0 :
    print(str(x) + " is an even number")

else :
    print(str(x) + " is an odd number")

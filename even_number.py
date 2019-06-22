# coding:utf-8
# The proposal of the exercice is to define whether the number is even or odd

x = "x"
print("The proposal of the exercice is to define whether the integer x is even or uneven.")

while True :
    try :
        x = int(input("Let's have "+ x +" = "))
        break
    except ValueError :
        print(x, "must be an integer ;) Try again...")

if x % 2 == 0 :
    print(str(x) + " is an even number")

else :
    print(str(x) + " is an uneven number")

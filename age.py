_author_ = "Mikus"

age = int(input("PLease enter your age:"))

print("Your age is :{}".format(age))

if age >= 18:
    print("You are eligible to vote")

    if age >= 65:
        print("You are a senior")
else:
    print("You will be eliigible to vote after {} years".format(18 - age))

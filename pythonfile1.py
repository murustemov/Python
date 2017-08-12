message = "Your age is"
age = 25

print(type(age))
print(message + ' ' + str(age))
print(type(str(age)))

print("Your age is {}, you are going to retire after {} years".format(age, 65 - age))
print("John is {0}, Mary is {1}, Bob is {0}, Sam is {1} years old".format(25,27))
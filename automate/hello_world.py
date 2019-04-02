#This program says hellow and asks for my name

print('Hello')
print('What is your name?')
myName=input()
print('Hello' + myName)
length=len(myName)
print('The length of your name is: ' + str(length) + ' characters')
print('What is your age?')
myAge=input()
print('You will be ' + str(int(myAge) + 1) + ' in a year')

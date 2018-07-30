import random
def hello(name):
    print('Hello ' + name)

hello('punk')
hello('pete')
hello('you')

def answer(number):
    if number == 1:
        return 'Yes'
    elif number == 2:
        return 'No'
    elif number == 3:
        return 'Maybe'
    else:
        return 'You ded'

print(answer(random.randint(1,5)))

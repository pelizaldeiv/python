catNames = []

while True:
    print('Enter the name of a cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print('The cats names are:')
for i in catNames:
    print(' '+i)

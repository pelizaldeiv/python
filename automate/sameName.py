def spam():
    global eggs
    eggs = 'spam'
def bacon():
    eggs = 'bacon'
def ham():
    print(eggs)

eggs = 'global'
ham()
spam()
print(eggs)

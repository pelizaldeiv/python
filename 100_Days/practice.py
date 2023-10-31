import sys

def print_letters(word):
    print(len(word))
    for j in range(len(word)):
        print(word[j])
    print("Hello " + input("what's your name? "))

if __name__ == '__main__':
    #globals()[sys.argv[1]]()
    print_letters(sys.argv[1])    
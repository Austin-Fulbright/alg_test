#!/whatever the fuck this is for


import sys


def countdown(n):    
    while n >= 0:
        print(n)
        n -= 1


def main():

    if len(sys.argv) != 2:
        print("countdown.py must be run with an arguement of <number>")
        sys.exit(1)


    try:
        num = int(sys.argv[1])

    except ValueError:
        print("Error: please enter a valid Integer")
        sys.exit(1)

    countdown(num)


if __name__ == '__main__':
    main()




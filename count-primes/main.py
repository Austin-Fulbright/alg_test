#a test:
import sys



def isPrime(n):
    isPrime = True
    for i in range(1, n):
        modded = n % i
        message = f"{n} % {i} = {modded}"
        print(message)
        if i != 1 and modded == 0:
            isPrime = False
    if isPrime:
        print(f"{n} is prime")
    else:
        print(f"{n} is not prime")
    return isPrime



def main():

    if len(sys.argv) != 2:
        print("give me a number in the arguements dipshit")
        sys.exit(1)

    try:
        num = int(sys.argv[1])
    except ValueError:
        print("try using a number as the arguement bud")
        sys.exit(1)
    
    isPrime(num)

if __name__ == '__main__':
    main()

#a test:
import sys



def count_primes(n):
    

    if n <= 2:
        return 0;

    prime_array = [True] * n

    prime_array[0] = prime_array[1] = False

    current = 2
    while current * current < n:

        if prime_array[current]:
            
            multiple = current * current


            while multiple < n:
                
                prime_array[multiple] = False
                multiple += current

        current += 1
    print(prime_array) 
    count = 0
    for i in range(n):
        if prime_array[i]:
            count+=1
    return count


def main():


    if len(sys.argv) != 2:
        print("give me a number in the arguements dipshit")
        sys.exit(1)

    try:
        num = int(sys.argv[1])
    except ValueError:
        print("try using a number as the arguement bud")
        sys.exit(1)

    the_count = count_primes(num)
    print(f"the number of primes inside of {num} is {the_count}")
    


if __name__ == '__main__':
    main()

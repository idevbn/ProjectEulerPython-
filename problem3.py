'''
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''


#Largest prime factor

def largest_prime_factor(n):
    """
    This function gets an input of a positive integer and returns its
    largest prime factor.
    """
    
    factor = 2 #first prime number
    
    while n < 2:
        n = int(input("Invalid input. Please enter a positive integer >= 2: "))
    
    while n > factor: 
        if n % factor == 0:
            n = n / factor #the factoring process continues

        else:
            factor += 1 #getting the next factor to test in the while loop

    return int(n)


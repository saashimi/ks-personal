# A program to obtain a list of prime numbers up to an input number.
# Usage: import to python interpreter.

__author__  = "Kevin Saavedra"

def list_primes(n):
    """Takes a list of numbers and returns a list of prime numbers up to the 
    input number.

    Example:
    --------
    list_primes(9) --> [1, 3, 5, 7]
    
    Parameters:
    -----------
    Input:
    n, an integer

    Output:
    lst: a list of prime numbers.
    """
    lst = []
    for num in range(2, n + 1): # Range starts at 2 to avoid 0/0 error and
                                # by definition, 1 is not a prime number.
                                # Ends at n+1 because range is inclusive.
        for denominator in range(2, num):
            if num % denominator == 0:  
                break
        else:
            lst.append(num)
              
    return lst
        

def factorial_(n):
    """Returns the factorial of n."""
    count = 1
    for elem in range(1, n+1):
        count *= elem

    return count

if __name__ == "___main___":
    n = eval(input("Please enter a number:   "))
    print(factorial_(n))

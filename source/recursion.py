#!python

def factorial(n):
    """factorial(n) returns the product of the integers 1 through n for n >= 0,
    otherwise raises ValueError for n < 0 or non-integer n"""
    # check if n is negative or not an integer (invalid input)
    if n < 0 or not isinstance(n, int):
        raise ValueError('function undefined for n < 0')
    if n == 1:
        return 1 
    factorial_number = n * factorial(n - 1)
    return factorial_number


def factorial_iterative(n):
    # TODO: implement the factorial function iteratively here
    empty_list = []
    counter = 1
    if n < 0:
        raise ValueError('function undefined for n < 0')

    if type(n) == float:
        raise ValueError('function undefined for float')
    
    # This is our base case
    if n == 1:
        return 1
    while n > 1:
        empty_list.append(n)
        n -= 1
    for number in empty_list:
            counter *= number

    return empty_list, counter

    # once implemented, change factorial (above) to call factorial_iterative
    # to verify that your iterative implementation passes all tests


def factorial_recursive(n):
    # check if n is one of the base cases
    if n == 0 or n == 1:
        return 1
    # check if n is an integer larger than the base cases
    elif n > 1:
        # call function recursively
        return n * factorial_recursive(n - 1)

def permutations(n,r):
    
    if n < 0 or r < 0:
        raise ValueError("function is undefined for n < 0 or r < 0")

    if r == 1:
        return 1
    
    return (n * permutations(n - 1)) / (r * permutations(r - 1))



def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 1:
        num = int(args[0])
        result = factorial(num)
        print('factorial({}) => {}'.format(num, result))
    else:
        print('Usage: {} number'.format(sys.argv[0]))




if __name__ == '__main__':
    # main()
    print(factorial_iterative(2.000))

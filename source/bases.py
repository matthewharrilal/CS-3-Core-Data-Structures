#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def transform_letter_into_integer(letter):
    hex_dict = {'0': 0,'1':1,'2':2, '3': 3, '4':4, '5': 5, '6': 6, '7': 7, '8':8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P':25, 'Q': 26, 'R': 27, 'S': 28, 'T':29, 'U':30, 'V':31,'W':32, 'X': 33, 'Y':34, 'Z': 35}
    return hex_dict[letter]


def encode_from_base_ten_to_any_base(digits, base):
    remainder_list = []
    remainder = digits % base

    print("This is the original dividend: %s, and the orignal remainder: %s" %(digits, remainder))

    while digits > base:

        digits //= base

        remainders = digits % base

        # Can not do this due to the reason that if we use this conditional then we are left with the problem that the quotient is left out
        # if digits != remainders:

        print("When the dividend is: %s, this is the remainder %s" %(digits ,remainders))
        remainder_list.append(remainders)
    print("This is the last number %s"%(remainder_list[-1]))
    remainder_list.remove(remainder_list[-1])
    # remainder_list.append(remainder)
    new_remainder_list = remainder_list[::-1]
    new_remainder_list.append(remainder)
    newer_list = [digits] + new_remainder_list
    return newer_list, str(newer_list)


# for _ in range(3):
#     print(divmod(8, 745))

def find_remainder(digits, base):
    return digits % base
print(encode_from_base_ten_to_any_base(23780273458, 8))


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # TODO: Decode digits from binary (base 2)
    # First things first we have to positon the digits that is beneifcial to us
    binary_digit_list = list(digits)

    # We need a count so we can increment it with the correct numbers
    binary_count = 0
    # Now that we have the list we have to work with the indexes

    len_of_binary_digit_list = len(binary_digit_list)

    # When decoding binary into integer the farthest number to the right is 2^ 0 multiplied by either 1 or 0
    # therefore we have to subtract 1 so we can get the strating value at index xero due to us raising the number to that power
    for index, digit in enumerate(binary_digit_list):
        power_postion = len_of_binary_digit_list - index
        binary_count += (base ** (power_postion - 1)) * digit
    return binary_count
    
    # ...
    # TODO: Decode digits from hexadecimal (base 16)
    hexadecimal_digit_list = list(digits.upper())

    hexadecimal_count = 0
    
    hex_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}    

    len_of_hexadecimal_digit_list = len(hexadecimal_digit_list)

    for index, hexdigit in enumerate(hexadecimal_digit_list):
        power_position = len_of_hexadecimal_digit_list - index
        if type(hexdigit) == str:
            hexadecimal_count +=  (base ** (power_position - 1) * transform_letter_into_integer(hexdigit))
        else:
            hexadecimal_count += (base ** (power_position - 1) * hexdigit)
    return hexadecimal_count

    # ...
    # TODO: Decode digits from any base (2 up to 36)
    # ...
    any_base_digit_list = list(digit.upper())

    cumalitive_count = 0

    len_of_digit_list = len(any_base_digit_list)


    for index, base_digit in enumerate(any_base_digit_list):
        power_position = len_of_digit_list - index
        if type(base_digit) == str and base > transform_letter_into_integer(base_digit):
            cumalitive_count += (base ** (power_position - 1) * transform_letter_into_integer(base_digit))
        else:
            return 'base is out of range: {}'.format(base)

    return cumalitive_count



def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)
    # ...
    # TODO: Encode number in hexadecimal (base 16)
    # ...
    # TODO: Encode number in any base (2 up to 36)
    # ...


    


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()

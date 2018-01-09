#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


# def transform_letter_into_integer(letter):
#     hex_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
#     return hex_dict[letter]


# def decode(digits):
#     hexadecimal_digit_list = list(digits)

#     hexadecimal_count = 0

#     len_of_hexadecimal_digit_list = len(hexadecimal_digit_list)
#     # pdb.set_trace()
#     for index, hexdigit in enumerate(hexadecimal_digit_list):
#         power_position = len_of_hexadecimal_digit_list - index
#         if type(hexdigit) == str:
#             hexadecimal_count += (2 ** (power_position - 1) * transform_letter_into_integer(hexdigit))
#         else:
#             print(type(hexdigit))
#             hexadecimal_count += (2 ** (power_position - 1) * hexdigit)

#     return hexadecimal_count

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
        binary_count += (2 ** (power_postion - 1)) * digit
    return binary_count
    
    # ...
    # TODO: Decode digits from hexadecimal (base 16)
    hexadecimal_digit_list = list(digits)

    hexadecimal_count = 0
    
    hex_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}    

    len_of_hexadecimal_digit_list = len(hexadecimal_digit_list)

    for index, hexdigit in enumerate(hexadecimal_digit_list):
        power_position = len_of_hexadecimal_digit_list - index
        # hexadecimal_count += (2 ** (power_position - 1) * hexdigit)
        for key, value in hex_dict.items():
            if hexdigit == key:
                hexadecimal_count += (2 ** (power_position - 1) ** value)
    return hexadecimal_count

    # ...
    # TODO: Decode digits from any base (2 up to 36)
    # ...


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

"""
Bin2Dec allows the user to enter strings of up to 8 binary digits, 0's and 1's, in any sequence and then displays its decimal equivalent.

This challenge requires that the developer implementing it follow these constraints:

    - Arrays may not be used to contain the binary digits entered by the user
    - Determining the decimal equivalent of a particular binary digit in the sequence must be calculated using a single mathematical function, 
    for example the natural logarithm. It's up to you to figure out which function to use.

Doc link: https://github.com/florinpop17/app-ideas/blob/master/Projects/1-Beginner/Bin2Dec-App.md
"""
TWO_POWER_ZERO  = 1
TWO_POWER_ONE   = 2
TWO_POWER_TWO   = 4
TWO_POWER_THREE = 8
TWO_POWER_FOUR  = 16
TWO_POWER_FIVE  = 32
TWO_POWER_SIX   = 64
TWO_POWER_SEVEN = 128
TWO_POWER_EIGHT = 256

# check if decimal is between two base 2 ranges
def convert_dec_to_binary(decimal):
    if decimal < TWO_POWER_ZERO or decimal > TWO_POWER_EIGHT:
        return None
    if decimal == 0:
        return 0
    if decimal < TWO_POWER_EIGHT and decimal > TWO_POWER_SEVEN:
        pass

user_input = int(input("Enter decimal integer (0 - 256) to convert to binary number"))

convert_dec_to_binary(user_input)

"""
1   =   2^0
2   =   2^1
4   =   2^2
8   =   2^3
16  =   2^4
32  =   2^5
64  =   2^6
128 =   2^7
256 =   2^8

user_input = 120,   base two = 2^7 - 2^3 = 120
user_input = 155,   base two = 2^8 - 2^6 - 2^5 - 2^2 - 2^0 = 155
"""
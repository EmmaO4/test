"""
Bin2Dec allows the user to enter strings of up to 8 binary digits, 0's and 1's, in any sequence and then displays its decimal equivalent.

This challenge requires that the developer implementing it follow these constraints:

    - Arrays may not be used to contain the binary digits entered by the user
    - Determining the decimal equivalent of a particular binary digit in the sequence must be calculated using a single mathematical function, 
    for example the natural logarithm. It's up to you to figure out which function to use.

Doc link: https://github.com/florinpop17/app-ideas/blob/master/Projects/1-Beginner/Bin2Dec-App.md

1   =   2^0
2   =   2^1
4   =   2^2
8   =   2^3
16  =   2^4
32  =   2^5
64  =   2^6             8       7       6       5       4       3       2       1       0              
128 =   2^7    ->       256     128     64      32      16      8       4       2       1 
256 =   2^8    |        0       0        1       1      1       1       0       0       0
               ^
user_input = 120,   base two = 2^7 - 2^3 = 120
user_input = 155,   base two = 2^8 - 2^6 - 2^5 - 2^2 - 2^0 = 155
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

binary_table_for_range_one = [0]
# check if decimal is between two base 2 ranges
# subtract the highest minimum base 2 without going under decimal 
def convert_dec_to_binary(decimal):
    range_one =     TWO_POWER_ZERO                                                      #  [1] 
    range_two =     ((decimal >= TWO_POWER_ONE) and (decimal < TWO_POWER_TWO))          #  [2 - 3] 
    range_three =   ((decimal >= TWO_POWER_TWO) and (decimal < TWO_POWER_THREE))        #  [4 - 7]
    range_four =    ((decimal >= TWO_POWER_THREE) and (decimal < TWO_POWER_FOUR))       #  [8 - 15]
    range_five =    ((decimal >= TWO_POWER_FOUR) and (decimal < TWO_POWER_FIVE))        #  [16 - 31]
    range_six =     ((decimal >= TWO_POWER_FIVE) and (decimal < TWO_POWER_SIX))         #  [32 - 63]
    range_seven =   ((decimal >= TWO_POWER_SIX) and (decimal < TWO_POWER_SEVEN))        #  [64 - 127]
    range_eight =   ((decimal >= TWO_POWER_SEVEN) and (decimal <= TWO_POWER_EIGHT))     #  [128 - 256]
    
    # helper fuction to calc highest minimum needed to compute recursive subtraction of base-two int of user input
    def calculate_highest_min(decimal):
        helper_decimal = decimal
        base_two_list = [TWO_POWER_ZERO, TWO_POWER_ONE, TWO_POWER_TWO, TWO_POWER_THREE, TWO_POWER_FOUR, TWO_POWER_FIVE, TWO_POWER_SIX, TWO_POWER_SEVEN, TWO_POWER_EIGHT]
        index_ref_list = []
        index = 8   
        for i in base_two_list[::-1]:
            if helper_decimal - i < 0:       # (120) - (256) < 0
                index -= 1
                continue
            else:
                index_ref_list.append(index)
                index -= 1
                helper_decimal = helper_decimal - i
        return index_ref_list[::-1]

    def convert(helper_decimal):
        binary_table = [0]*8
        index_table = calculate_highest_min(helper_decimal)
        binary = ''
        for i in range(len(binary_table)):
            for j in range(len(index_table)):
                # binary_table index value += 1 where index matches index value of index_table 
                if i == index_table[j]:
                    binary_table[i - 1] += 1    # this works but index error when using other user inputs that match at binary_table index 0
        for bit in binary_table:
            binary += str(bit)
        
        print(f'{decimal} to binary: {binary}')


    if decimal > TWO_POWER_EIGHT:
        return None                         # want this to return error message
    if decimal <= 0: 
        return 0
    # this bugs cause range_one is a truthy value that always outputs true > this will print in addition to resulting range from user input
    # "if true:" -- where 1 is always true
    if decimal == range_one:                           # input = 1, output = 1
        print(binary_table_for_range_one)
    if range_two:                           # input = 2, output = 10
        convert(decimal)
    if range_three:                         # input = 5, output = 101
        convert(decimal)
    if range_four:                          # input = 12, output = 1100
        modify = 4
        binary_table = [0]*modify
        print(binary_table)
    if range_five:                          # input = 20, output = 10100
        modify = 5
        binary_table = [0]*modify
        print(binary_table)
    if range_six:                           # input = 55, output = 110111
        modify = 6
        binary_table = [0]*modify
        print(binary_table)
    if range_seven:                         # input = 120, output = 1111000
        convert(decimal)
        
    if range_eight:                         # input = 217, output = 11011001
        modify = 8
        binary_table = [0]*modify
        print(binary_table)
    
    
user_input = int(input("Enter decimal integer (0 - 256) to convert to binary number: "))

convert_dec_to_binary(user_input)
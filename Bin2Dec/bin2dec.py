"""
Bruh I did this backwards. added a convert_binary_to_decimal() function to complete this correctly works correctly. 

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
64  =   2^6             7      6       5       4       3       2       1       0              
128 =   2^7    ->      128     64      32      16      8       4       2       1 
256 =   2^8    |        0       0       1      1       0       1       1       1
               ^
user_input = 120,   base two = 2^7 - 2^3 = 120
user_input = 155,   base two = 2^8 - 2^6 - 2^5 - 2^2 - 2^0 = 155
"""
import time

TWO_POWER_ZERO  = 1
TWO_POWER_ONE   = 2
TWO_POWER_TWO   = 4
TWO_POWER_THREE = 8
TWO_POWER_FOUR  = 16
TWO_POWER_FIVE  = 32
TWO_POWER_SIX   = 64
TWO_POWER_SEVEN = 128 

binary_table_for_range_one = [0]
# check if decimal is between two base 2 ranges
# subtract the highest minimum base 2 without going under decimal 
def convert_decimal_to_binary(decimal):
    range_one =     TWO_POWER_ZERO                                                      #  [1] 
    range_two =     ((decimal >= TWO_POWER_ONE) and (decimal < TWO_POWER_TWO))          #  [2 - 3] 
    range_three =   ((decimal >= TWO_POWER_TWO) and (decimal < TWO_POWER_THREE))        #  [4 - 7]
    range_four =    ((decimal >= TWO_POWER_THREE) and (decimal < TWO_POWER_FOUR))       #  [8 - 15]
    range_five =    ((decimal >= TWO_POWER_FOUR) and (decimal < TWO_POWER_FIVE))        #  [16 - 31]
    range_six =     ((decimal >= TWO_POWER_FIVE) and (decimal < TWO_POWER_SIX))         #  [32 - 63]
    range_seven =   ((decimal >= TWO_POWER_SIX) and (decimal <= TWO_POWER_SEVEN))        #  [64 - 128]
    
    # helper fuction to calc highest minimum needed to compute recursive subtraction of base-two int of user input
    def calculate_highest_min(decimal):
        helper_decimal = decimal
        base_two_list = [TWO_POWER_ZERO, TWO_POWER_ONE, TWO_POWER_TWO, TWO_POWER_THREE, TWO_POWER_FOUR, TWO_POWER_FIVE, TWO_POWER_SIX, TWO_POWER_SEVEN]
        index_ref_list = []
        index = 8
        # print(base_two_list[::-1])
        for i in base_two_list[::-1]:
            if helper_decimal - i < 0:       # (55) - (126) < 0
                index -= 1
                continue
            else:
                index_ref_list.append(index)
                index -= 1
                helper_decimal = helper_decimal - i
        # print(index_ref_list)
        return index_ref_list[::-1]

    def convert(helper_decimal):
        binary_table = [0]*8
        # print(binary_table)
        index_table = calculate_highest_min(helper_decimal)
        
        for i in range(len(binary_table)):
            for j in range(len(index_table[::-1])):
                # binary_table index value += 1 where index matches index value of index_table 
                if i == index_table[j]:     # (0) == (6) 
                    binary_table[i - 1] += 1    # this works but index error when using other user inputs that match at binary_table index 0
        
        binary_string = ''
        # print(binary_table)
        for bit in binary_table[::-1]:
            binary_string += str(bit)
        
        binary = ''
        indx = 0
        # print(binary_string)

        if binary_string.startswith('0'):
            i = 0
            while binary_string[i] == '0':
                i += 1
                if binary_string[i] == '1':
                    indx = i
                    break
        # print(f'print starting from index: {indx} \nbinary: {binary_string}')
        for i in range(indx, len(binary_string)):
            binary += str(binary_string[i])
        print(f'{decimal} to binary: {binary}')

    if decimal > TWO_POWER_SEVEN:
        print("Invalid input")                         # want this to return error message
    if decimal <= 0: 
        print(f'{decimal} to binary: {0}')  # input = 0, output = 0
    # this bugs cause range_one is a truthy value that always outputs true > this will print in addition to resulting range from user input
    # "if true:" -- where 1 is always true                 

    if decimal == range_one:                # input = 1, output = 1
        print(f'{decimal} to binary: {1}')
    if range_two:                           # input = 2, output = 00000010 = 10
        convert(decimal)
    if range_three:                         # input = 5, output = 00000101 = 101
        convert(decimal)
    if range_four:                          # input = 12, output = 00001100 = 1100
        convert(decimal)
    if range_five:                          # input = 20, output = 00010100 = 10100
        convert(decimal)
    if range_six:                           # input = 55, output = 00110111 = 110111
        convert(decimal)
    if range_seven:                         # input = 120, output = 1111000
        convert(decimal)
            
def convert_binary_to_decimal(binary):
    initial_list = []
    for bit in str(binary):
        initial_list.append(int(bit))
    # print(initial_list)

    # check index count of initial_list 
    if len(initial_list) < 8:
        index_count = 8 - len(initial_list) 
        rev_initial_list = initial_list[::-1]
        
        # flip initial_list to append 0 bits to end then flip again to keep original value in binary
        for i in range(index_count):
            rev_initial_list.append(0)
        initial_list = rev_initial_list[::-1]
        # print(initial_list)

        string_binary = ''

        for digit in initial_list:
            string_binary += str(digit)
            # int_binary = int(list_to_int)

        # print(f'binary in string format: {string_binary}')

        # assign initial_list index to two_base values from powers: 0 - 7
        initial_list[0] = TWO_POWER_SEVEN
        initial_list[1] = TWO_POWER_SIX
        initial_list[2] = TWO_POWER_FIVE
        initial_list[3] = TWO_POWER_FOUR
        initial_list[4] = TWO_POWER_THREE
        initial_list[5] = TWO_POWER_TWO
        initial_list[6] = TWO_POWER_ONE
        initial_list[7] = TWO_POWER_ZERO

        # read initial_list -> for every index where bit == 1: add the two_base power value
        truthy_bypass = 1
        binary_rolling_sum = 0

        # print(f'binary first bit: {string_binary[5]}')
        # print(f'initial list first bit: {initial_list[5]}')
        
        # calc bit sum for decimal conversion
        for i in range(len(string_binary)):
            # print(string_binary[i])
            if string_binary[i] == str(truthy_bypass): # truthy didn't work here?
                binary_rolling_sum += initial_list[i]
                # print(f'{binary_rolling_sum} + {initial_list[i]}')
        print(f'{binary} to decimal: {binary_rolling_sum}')

print("MENU")
print("1. Convert Binary to Decimal")
print("2. Convert Decimal to Binary")
print("0. Exit")
print("********************\n")
user_input = int(input("Enter option number: "))

while user_input != 0:
    if user_input == 1:
        binary_convert = input("Enter Binary: ")
        convert_binary_to_decimal(binary_convert)
        break
    elif user_input == 2:
        decimal_convert = str(input("Enter Decimal: "))
        convert_decimal_to_binary(decimal_convert)
        break
    else:
        print("invalid input ")

# start_time = time.perf_counter()            # start timer
# # program goes here
# end_time = time.perf_counter()              # end timer
# elapsed_time = end_time - start_time

# print(f"Program runtime: {elapsed_time:.8f} seconds")

"""
TODO
    research optimal algorithms for his prob - practice those
    
    add functions:
        binary calculator 
        optimize code heavy
    DONE
        elim leading 0s  
        make CLI to select between bin to dec or vice versa
"""
# runtime: O(1) 
# space:   O(1) 
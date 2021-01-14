# Convert an Integer into its Binary

# Division by 2 can be used to compute the binary equivalent
#   - Keep dividing by 2 and store its remainder until the dividend reaches 0
#   - List the remainders in opposite order to create the binary equivalent

from stack import Stack

def convert_int_to_bin(dec_num):
    s = Stack()

    dec_num = int(dec_num)

    while (dec_num > 0):
        remainder = dec_num % 2
        dec_num = dec_num // 2
        s.push(remainder)

    bin_num = ""
    while (not s.is_empty()):
        bin_num += str(s.pop())

    return bin_num

print(convert_int_to_bin("242"))


# Reversing a string can be accomplished by ...

random_str = "baby"
print(random_str[::-1])

# Reversing a string can be done through a stack

from stack import Stack

def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])
    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()
    return rev_str

print(reverse_string(Stack(), "!evitacudE ot emocleW"))
# Determine if Brackets are Balanced

# Balanced brackets = {}, {}{}, (({[]}))
# Unbalanced brackets = ((), {{{)}], [][]]]

# Iterate through characters of string
# If opening bracket, push onto stack
# If closing bracket, pop off stack and match it with closing bracket
#   - If opening bracket == closing bracket, balanced for now
#   - If not, unbalanced brackets
# Stack will be empty after end of iteration

# Special case where )) doesn't have any elements to pop off from the stack 
#   - must check the stack empty of not before popping

from stack import Stack

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False

def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else: 
            if s.is_empty():
                is_balanced = False
            else: 
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else: 
        return False

print("String : (((({})))) Balanced or not?")
print(is_paren_balanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_paren_balanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_paren_balanced("[][]"))
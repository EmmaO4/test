tokens = list("+-aaa")  # input string – derived grammar

def parse():
    token = tokens.pop(0)        # first token
    if token == 'a':             # rule S -> a
        return "a"
    elif token in ('+', '-'):    # rule S -> +SS
        left = parse()       # parse s w/ recursion
        right = parse()      # parse next s w/ recursion
        return (token, left, right)
    else:
        raise ValueError("Unexpected token: " + token) # exception handling

tree = parse()
print(tree)
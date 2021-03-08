input = {'key1': 1,'key2': {'key3': 1, 'key4': { 'key5': 4}}}

def print_depth(input, depth):
    depth = depth + 1
    
    for i in input:
        if isinstance(input.get(i), dict):
            print(i, ' ', depth)
            print_depth(input.get(i), depth)
        else:
            print(i, ' ', depth)
    
    depth = depth - 1


print_depth(input, 0)

import inspect

class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

person_a = Person('User', '1', None)
person_b = Person('User', '2', person_a)

input = {   'key1': 1,
            'key2': {
                'key3': 1,
                'key4': {
                    'key5': 4,
                    'user': person_b,
                    }
                },
        }

def print_depth(input, depth):
    depth = depth + 1
    
    for i in input:
        if isinstance(input.get(i), dict):
            print(i, ' ', depth)
            print_depth(input.get(i), depth)
        elif type(input.get(i)) == type(person_a):
            print(i, ' ', depth)
            if_person(input.get(i), depth + 1)
        else:
            print(i, ' ', depth)
    
    depth = depth - 1

def if_person(person, depth):
    for i in inspect.getmembers(person)[2][1].keys():
            print(i, ' ', depth)
            
    if type(person.father) == type(person_a):
        if_person(person.father, depth + 1)
                

print_depth(input, 0)

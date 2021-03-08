# Time complexity: O(n1) + O(n2) because there are mainly two loops.
# suppose one loop runs n1 times another n2 times. 
# Space complexity: O(n) + C, here n is the size of tree and 
# C is the size of 2 inputs.


from math import floor
tree = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


node1 = input('Enter first node: ')
node2 = input('Enter second node: ')

def get_parents(node):
    parents = []
    parents.append(node)
    if(node > 1):
        while node > 0:
            node = floor(node / 2)
            if node > 0:
                parents.append(node)
    return parents

def lca(node1, node2):
    parents1 = get_parents(int(node1))
    parents2 = get_parents(int(node2))

    if(len(parents2) > len(parents1)):
        l = len(parents1)
        for i in range(0, l):
            if parents1[i] in parents2:
                print(parents1[i])
                return parents1[i]
            
    else:
        l = len(parents2)
        for i in range(0, l):
            if parents2[i] in parents1:
                print(parents2[i])
                return parents2[i]
            

lca(node1, node2)



# The logic is bit hard to understand. I have to think about it again.
# I got the solution from the internet.

billion = 1000000000
nodes = [((-1 * billion, billion), 1)]

number_of_elements = int(input())
elements = map(int, input().split())

def search_node(value):
    result = tuple()
    
    for node in nodes:
        if node[0][0] < value <= node[0][1]:
            result = node
            nodes.remove(result)
            return result


for element in elements:
    node = search_node(element)
    
    left = node[0][0]
    right = node[0][1]
    level = node[1]
    
    nodes.insert(0, ((left, element), level + 1))
    nodes.insert(1, ((element, right), level + 1))
    print(level, end=' ')
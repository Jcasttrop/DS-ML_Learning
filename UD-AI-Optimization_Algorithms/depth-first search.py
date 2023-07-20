class Node:
    def __init__(self,name):
        self.name = name
        self.adjacencyList = [] # list of nodes that are connected to this node
        self.visited = False # to keep track of whether we have visited this node or not

def depth_first_search(start_node):

    #we need a LIFO: last in first out data structure

    stack = [start_node]

    while stack:

        actual_node = stack.pop()
        actual_node.visited = True
        print(actual_node.name)

        for n in actual_node.adjacencyList:
            if not n.visited: # if the node has not been visited so far
                stack.append(n) # add it to the stack

if __name__ == '__name__':
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    node1.adjacencyList.append(node2)
    node1.adjacencyList.append(node3)
    node2.adjacencyList.append(node4)
    node4.adjacencyList.append(node5)

    depth_first_search(node1)
    

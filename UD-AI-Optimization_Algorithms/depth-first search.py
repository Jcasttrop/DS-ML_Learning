class Node:
    def __init__(self,name):
        self.name = name
        self.adjacencyList = [] # list of nodes that are connected to this node
        self.visited = False # to keep track of whether we have visited this node or not

def depth_first_search_stack(start_node):

    #we need a LIFO: last in first out data structure

    stack = [start_node]

    while stack:

        actual_node = stack.pop()
        actual_node.visited = True
        print(actual_node.name)

        for n in actual_node.adjacencyList:
            if not n.visited: # if the node has not been visited so far
                stack.append(n) # add it to the stack


def depth_first_search_recursive(node):

    node.visited = True
    print(node.name)

    for n in node.adjacencyList:
        if not n.visited:
            depth_first_search_recursive(n)


if __name__ == '__main__':

    node_1 = Node("A")
    node_2 = Node("B")
    node_3 = Node("C")
    node_4 = Node("D")
    node_5 = Node("E")

    node_1.adjacencyList.append(node_2)
    node_1.adjacencyList.append(node_3)
    node_2.adjacencyList.append(node_4)
    node_4.adjacencyList.append(node_5)
    
    depth_first_search_stack(node_1)
    depth_first_search_recursive(node_1)

    



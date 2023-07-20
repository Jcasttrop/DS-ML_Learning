class Node:
    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False


def breadth_first_search(start_node):

    #queue is FIFO
    queue = [start_node]
    actual_node.visited = True
    #we keep iterating (considering the neighbors) until the queue becomes empty
    while queue:
        actual_node = queue.pop(0) #remove and return the first element in the list
        print(actual_node.name)

        #let's consider the neighbors of the actual node one by one

        for n in actual_node.adjacency_list:
            if not n.visited:
                n.visited = True
                queue.append(n)

if __name__ == '__main__':
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    
    #we have to handle the neighbors of each node
    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node4.adjacency_list.append(node5)

    #run the algorithm
    breadth_first_search(node1)
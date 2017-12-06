class Node(object):
    '''
    Linked lists are made up of nodes,
    - [data,  ] -> [data, ]
    '''
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return "Node({!r})".format(self.data)

node = Node('test')
print(node)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

'''
To link the nodes, we have to make the first node refer to
the second and the second node refer to the third:
'''
node1.next = node2
node2.next = node3

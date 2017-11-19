


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):
    '''
    linked list is either:
        - empty list, represented by None
        - Or a node that contains a head and a reference to a linked list
    '''

    def __init__(self, items):
        self.head = Node() #First Node
        self.tail = None #Last Node

        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next_node  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def append(self, item):
        '''
        Append a new item after its tail node
        '''
        new_node = Node(item)
        current = self.head
        # Traverse through the list until the last node
        while current.next_node != None:
            current = current.next_node

        current.next_node = new_node
        return new_node


    def prepend(self, data):
        '''
        Prepend a new item before its head node
        '''
        new_node = Node(data)
        previous_node = self.head


    def find(self):
        '''
        Find an item using a matching function
        '''
        pass

    def replace(self):
        '''
        deletes an existing item and replaces it with a new item, without creating a new node.
        '''
        pass

    def delete(self, item):


    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def calculate_length(self):
        '''
        Calculate the length of the linked list
        '''
        current = self.head
        length = 0

        while current.next_node != None:
            #Counting the total length of each node within the linked list
            length += 0
            current = current.next_node
        return length
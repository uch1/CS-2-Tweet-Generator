


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

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
        self.head = None #First Node
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
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def append(self, item):
        '''
        Append a new item after its tail node
        '''
        new_node = Node(item)
        current = self.head
        # Traverse through the list until the last node
        while current.next != None:
            current = current.next

        current.next = new_node
        return new_node


    def prepend(self, item):
        '''
        Prepend a new item before its head node
        '''
        new_node = Node(item)

        if self.is_empty():
            self.head = new_node
            self.tail = self.head
        else:
            #new node should point to the old node(head)
            #head should be the new node
            new_node.next = self.head
            self.head = new_node


    def find(self, quality):
        '''
        Find an item using a matching function
        '''
        node = self.head

        while node != None:
            if quality(node.data):
                return node.data
            node = node.next

    def replace(self):
        '''
        deletes an existing item and replaces it with a new item, without creating a new node.
        '''
        pass

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError."""
        current = self.head
        previous = None

        while current is not None:
            if current.data == item:
                if current is not self.head and current is not self.tail:
                    previous.next = current.next
                    current.next = None
                if current is self.head:
                    self.head = current.next
                    current.next = None
                if current is self.tail:
                    if previous is not None:
                        previous.next = None
                    self.tail = previous
                return current
            # Update previous node to skip around node with matching data
            previous = current
            current = current.next
        raise ValueError('Item not found: {}'.format(item))

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



def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()

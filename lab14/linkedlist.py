"""
    Description: Implementation of a linked list relying on the Node class.
    A linked list is a collection of objects/nodes, where each node contains both
    the item stored in the list, as well as a “pointer” to the next node in the list.
    Author: Matthew Erdman
    Date: 11/18/21
"""
from node import *

class LinkedList(object):
    """ class for a linked list composed of mulitple Node objects linked to each other """

    def __init__(self):
        """ construct an empty linked list """
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        """ return string representation of linked list """
        string = "["
        n = self.head
        for i in range(self.size):
            string += ("%s, " % str(n.getItem())) # Traverse list to build up string
            n = n.getNext()                       # Move to next item in list
        if not self.isEmpty():
            string = string[:-2] # Trim dangling comma and space on last element
        string += "]"
        return string

    def __len__(self):
        """ return length of linked list """
        return self.size

    def __contains__(self, item):
        """ return True if a given item is in the linked list """
        return self.index(item) != -1 # True if index() is able to find item

    def __getitem__(self, index):
        """ return the item at the given index """
        item = None
        if 0 <= index < self.size: # Ensure index is within list bounds
            n = self.head
            for i in range(index): # Traverse list to desired index
                n = n.getNext()
            item = n.getItem()
        return item # Returns None if index OOB

    def __setitem__(self, index, item):
        """ sets the item at the given index """
        if 0 <= index < self.size: # Ensure index is within list bounds
            n = self.head
            for i in range(index): # Traverse list to given element
                n = n.getNext()
            n.setItem(item)
        return

    def isEmpty(self):
        """ return a boolean indicating whether the list is empty """
        return self.size == 0

    def append(self, item):
        """ take a string and add it as an element to the end of the linked list """
        new = Node(item)
        if self.isEmpty():
            self.head = new # Element added to an empty list becomes head and tail
        else:
            self.tail.setNext(new) # List isn't empty, add pointer to new element
        self.tail = new
        self.size += 1
        return

    def prepend(self, item):
        """ take a string and add it as an element to the start of the linked list """
        new = Node(item)
        if self.isEmpty():
            self.tail = new # Element added to an empty list becomes head and tail
        new.setNext(self.head) # Will set next to None if list empty
        self.head = new
        self.size += 1
        return

    def deleteHead(self):
        """ delete first element of linked list, returning the item it contained """
        oldHead = None
        if not self.isEmpty():
            oldHead = self.head.getItem() # Stored to return item later
            if self.size == 1:
                # A 1 element list will now be empty
                self.head = None
                self.tail = None
            else:
                # Multiple items, shift head down
                self.head = self.head.getNext()
            self.size -= 1
        return oldHead # Returns None if list is empty

    def deleteTail(self):
        """ delete last element of linked list, returning the item it contained """
        oldTail = None
        if not self.isEmpty():
            oldTail = self.tail.getItem() # Stored to return item later
            if self.size == 1:
                # A 1 element list will now be empty
                self.head = None
                self.tail = None
            else:
                # Multiple items, shift tail up
                n = self.head
                for i in range(self.size-2): # Get second to last element
                    n = n.getNext()
                self.tail = n # Replace tail element with second to last element
                self.tail.setNext(None)
            self.size -= 1
        return oldTail # Returns None if list is empty

    def count(self, item):
        """ return the number of occurrences of a given item in the linked list """
        n = self.head
        count = 0
        for i in range(self.size): # Traverse every element in list
            if n.getItem() == item:
                count += 1 # Increment counter if given item matches
            n = n.getNext()
        return count

    def index(self, item):
        """
        return index of first occurrence of a given item in the linked list,
        or -1 if item not found
        """
        n = self.head
        index = -1
        for i in range(self.size): # Traverse through list
            if n.getItem() == item:
                index = i
                break # Escape loop on first instance of item found
            n = n.getNext()
        return index # Returns -1 if item is not in list

    def insert(self, index, item):
        """ insert given string as an element at given index in linked list """
        # Negative index will be ignored
        if index == 0:
            # Inserting as first element, use prepend()
            self.prepend(item)
        elif index >= self.size:
            # Inserting as last element, use append()
            self.append(item)
        elif 0 < index < self.size - 1:
            # Inserting in the middle, traverse list
            prev = self.head
            for i in range(index-1): # prev will be element immediately before index
                prev = prev.getNext()
            new = Node(item)
            new.setNext(prev.getNext()) # New element points to next element in list
            prev.setNext(new)           # Previous element points to new element
            self.size += 1
        return

    def pop(self, index):
        """ remove the element at a given index, returning the item contained """
        item = None
        if index == 0:
            # Pop first element, use deleteHead()
            item = self.deleteHead()
        elif index == self.size-1:
            # Pop last element, use deleteTail()
            item = self.deleteTail()
        elif 0 < index < self.size - 1:
            # Pop in the middle, traverse list
            prev = self.head
            for i in range(index-1): # prev will be element immediately before index
                prev = prev.getNext()
            n = prev.getNext() # n is element to pop
            prev.setNext(n.getNext()) # Set prev to point past popped element
            self.size -= 1
            item = n.getItem()
        return item # Returns None if index OOB

    def remove(self, item):
        """ remove first occurrence of given item in linked list """
        self.pop(self.index(item)) # pop() receives and ignores -1 if item not found
        return


if __name__ == "__main__":
    # Test prepend method
    LL = LinkedList()
    print("\nTesting prepend()...")
    print("List: " + str(LL))
    LL.prepend("B")
    print("Prepending B: " + str(LL))
    LL.prepend("A")
    print("Prepending A: " + str(LL))
    assert len(LL) == 2
    assert str(LL) == "[A, B]"

    # Test deleteHead method
    print("\nTesting deleteHead()...")
    print("List: " + str(LL))

    head1 = LL.deleteHead()
    print("Deleted head 1: " + head1)
    print("List: " + str(LL))
    assert head1 == "A"

    head2 = LL.deleteHead()
    print("Deleted head 2: " + head2)
    print("List: " + str(LL))
    assert head2 == "B"

    head3 = LL.deleteHead()
    print("Deleted head 3: " + str(head3))
    print("List: " + str(LL))
    assert head3 == None

    assert str(LL) == "[]"
    assert len(LL) == 0

    # Test append method
    LL = LinkedList()
    print("\nTesting append()...")
    print("List: " + str(LL))
    LL.append("A")
    print("Appending A: " + str(LL))
    LL.append("B")
    print("Appending B: " + str(LL))
    assert len(LL) == 2
    assert str(LL) == "[A, B]"

    # Test deleteTail method
    print("\nTesting deleteTail()...")
    print("List: " + str(LL))

    tail1 = LL.deleteTail()
    print("Deleted tail 1: " + tail1)
    print("List: " + str(LL))
    assert tail1 == "B"

    tail2 = LL.deleteTail()
    print("Deleted tail 2: " + tail2)
    print("List: " + str(LL))
    assert tail2 == "A"

    tail3 = LL.deleteTail()
    print("Deleted tail 3: " + str(tail3))
    print("List: " + str(LL))
    assert tail3 == None

    assert str(LL) == "[]"
    assert len(LL) == 0

    # Test insert method
    print("\nTesting insert()...")
    print("List: " + str(LL))

    LL.insert(-2, "A")
    print("Inserting A at index -2: " + str(LL))

    LL.insert(0, "B")
    print("Inserting B at index 0: " + str(LL))

    LL.insert(0, "A")
    print("Inserting A at index 0: " + str(LL))

    LL.insert(10, "C")
    print("Inserting C at index 10: " + str(LL))

    LL.insert(2, "B")
    print("Inserting B at index 2: " + str(LL))

    assert len(LL) == 4
    assert str(LL) == "[A, B, B, C]"

    # Test count method
    print("\nTesting count()...")
    print("List: " + str(LL))

    countC = LL.count("C")
    print("C count: " + str(countC))
    assert countC == 1

    countB = LL.count("B")
    print("B count: " + str(countB))
    assert countB == 2

    countFace = LL.count(":)")
    print(":) count: " + str(countFace))
    assert countFace == 0

    # Test index method
    print("\nTesting index()...")
    print("List: " + str(LL))

    indexA = LL.index("A")
    print("A index: " + str(indexA))
    assert indexA == 0

    indexB = LL.index("B")
    print("B index: " + str(indexB))
    assert indexB == 1

    indexC = LL.index("C")
    print("C index: " + str(indexC))
    assert indexC == 3

    indexFace = LL.index(":(")
    print(":( index: " + str(indexFace))
    assert indexFace == -1

    # Test pop method
    print("\nTesting pop()...")
    print("List: " + str(LL))

    pop1 = LL.pop(10)
    print("Popped index 10: " + str(pop1))
    print(LL)
    assert pop1 == None

    pop2 = LL.pop(0)
    print("Popped index 0: " + str(pop2))
    print(LL)
    assert pop2 == "A"

    pop3 = LL.pop(2)
    print("Popped index 2: " + str(pop3))
    print(LL)
    assert pop3 == "C"

    pop4 = LL.pop(1)
    print("Popped index 1: " + str(pop4))
    print(LL)
    assert pop4 == "B"

    pop5 = LL.pop(0)
    print("Popped index 0: " + str(pop5))
    print(LL)
    assert pop5 == "B"

    pop6 = LL.pop(0)
    print("Popped index 0: " + str(pop6))
    print(LL)
    assert pop6 == None

    assert str(LL) == "[]"
    assert len(LL) == 0

    # Test remove method
    print("\nTesting remove()...")
    LL.append("A")
    LL.append("B")
    LL.append("B")
    print("List: " + str(LL))

    LL.remove("B")
    print("Removing B: " + str(LL))

    LL.remove("A")
    print("Removing A: " + str(LL))

    LL.remove(":0")
    print("Removing \":0\": " + str(LL))

    LL.remove("B")
    print("Removing B: " + str(LL))

    LL.remove("A")
    print("Removing A: " + str(LL))

    assert str(LL) == "[]"
    assert len(LL) == 0

    # Test __contains__ method
    print("\nTesting __contains__ (in operator)...")
    LL.append("A")
    LL.append("B")
    print("List: " + str(LL))

    contains1 = "A" in LL
    print("Contains A: " + str(contains1))
    assert contains1

    contains2 = ":$" in LL
    print("Contains \":$\": " + str(contains2))
    assert not contains2

    print("Testing with empty list...")
    LL.deleteHead()
    LL.deleteHead()
    print("List: " + str(LL))

    contains3 = "A" in LL
    print("Contains A: " + str(contains3))
    assert not contains3

    # Test __getitem__ method
    print("\nTesting __getitem__...")
    LL.append("A")
    LL.append("B")
    print("List: " + str(LL))

    print("Index 0 contains: " + LL[0])
    assert LL[0] == "A"

    print("Index 1 contains: " + LL[1])
    assert LL[1] == "B"

    print("Index 10 contains: " + str(LL[10]))
    assert LL[10] == None

    print("Testing with empty list...")
    LL.deleteHead()
    LL.deleteHead()
    print("List: " + str(LL))

    print("Index 0 contains: " + str(LL[0]))
    assert LL[0] == None

    # Test __setitem__ method
    print("\nTesting __setitem__...")
    LL.append("A")
    LL.append("B")
    print("List: " + str(LL))

    LL[0] = "C"
    print("Setting index 0 to C: " + str(LL))

    LL[1] = "A"
    print("Setting index 1 to A: " + str(LL))

    LL[2] = "D"
    print("Setting index 2 to D: " + str(LL))

    assert str(LL) == "[C, A]"
    assert len(LL) == 2

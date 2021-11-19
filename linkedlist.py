from node import *

class LinkedList(object):

    def __init__(self):
        """ construct an empty linked list """
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        """ return string representation of linked list """
        s = "["
        curr = self.head
        for i in range(self.size):
            s += ("%s, " % str(curr.getItem()))
            curr = curr.getNext()
        if not self.isEmpty():
            s = s[:-2]
        s += "]"
        return s

    def __len__(self):
        """ return length of linked list """
        return self.size

    def __contains__(self, item):
        """ return True if a given item is in the linked list """
        return self.index(item) != -1

    def __getitem__(self, index):
        """ return the item at the given index """
        if 0 <= index < self.size: # Ensure index is within list bounds
            n = self.head
            for i in range(index):
                n = n.getNext()
            return n.getItem()
        return None # Only reached if index OOB

    def __setitem__(self, index, item):
        """ sets the item at the given index """
        if 0 <= index < self.size: # Ensure index is within list bounds
            n = self.head
            for i in range(index):
                n = n.getNext()
            n.setItem(item)

    def isEmpty(self):
        return self.size == 0

    def append(self, item):
        """ take a string and add it as an element to the end of the linked list """
        new = Node(item)
        if self.isEmpty():
            self.head = new # Element added to empty list becomes head and tail
        else:
            self.tail.setNext(new) # List isn't empty, add on the element
        self.tail = new
        self.size += 1

    def prepend(self, item):
        """ take a string and add it as an element to the start of the linked list """
        new = Node(item)
        if self.isEmpty():
            self.tail = new # Element added to empty list becomes head and tail
        new.setNext(self.head) # Will set next to None if list empty
        self.head = new
        self.size += 1

    def deleteHead(self):
        """ delete the first element of the linked list, returning the item it contained """
        if not self.isEmpty():
            oldHead = self.head.getItem() # Stored to return later
            if self.size == 1:
                # 1 element list will now be empty
                self.head = None
                self.tail = None
            else:
                # Multiple items, shift head down
                self.head = self.head.getNext()
            self.size -= 1
            return oldHead
        return None # Only reached if list is empty

    def deleteTail(self):
        """ delete the last element of the linked list, returning the item it contained """
        if not self.isEmpty():
            oldTail = self.tail.getItem() # Stored to return later
            if self.size == 1:
                # 1 element list will now be empty
                self.head = None
                self.tail = None
            else:
                # Multiple items, shift tail up
                n = self.head
                for i in range(self.size-2): # Get second to last element
                    n = n.getNext()
                self.tail = n
            self.size -= 1
            return oldTail
        return None # Only reached if list is empty

    def count(self, item):
        """ return the number of occurrences of a given item in the linked list """
        n = self.head
        count = 0
        # Linear search through every element in list
        for i in range(self.size):
            if n.getItem() == item:
                count += 1
            n = n.getNext()
        return count

    def index(self, item):
        """ return the index of the first occurrence of a given item in the linked list """
        n = self.head
        # Linear search through every element in list
        for i in range(self.size):
            if n.getItem() == item:
                return i
            n = n.getNext()
        return -1 # Only reached if item is not in list

    def insert(self, index, item):
        """ insert a given string as an element at a given index in the linked list """
        if index == 0:
            # Inserting as first element, use prepend()
            self.prepend(item)
        elif index == self.size:
            # Inserting as last element, use append()
            self.append(item)
        elif 0 < index < self.size:
            # Inserting in the middle, crawl through list
            prev = self.head
            for i in range(index-1): # prev will be node immediately before desired index
                prev = prev.getNext()
            new = Node(item)
            new.setNext(prev.getNext()) # New node points to next element in list
            prev.setNext(new)           # Previous node points to new node
            self.size += 1

    def pop(self, index):
        """ return the item at a given index, removing the element """
        if index == 0:
            # Pop first element, use deleteHead()
            return self.deleteHead()
        elif index == self.size-1:
            # Pop last element, use deleteTail()
            return self.deleteTail()
        elif 0 < index < self.size:
            # Pop in the middle, crawl through list
            prev = self.head
            for i in range(index-1): # prev will be node immediately before desired index
                prev = prev.getNext()
            n = prev.getNext() # n is the node to pop
            prev.setNext(n.getNext()) # Set prev element to point past n
            self.size -= 1
            return n.getItem()
        return None # Only reached if index OOB

    def remove(self, item):
        """ remove the first occurrence of a given item in the linked list """
        self.pop(self.index(item)) # If item not found, index will return -1 to pop


if __name__ == "__main__":
    # Test linked list initialization
    print("Testing initialization...")
    LL = LinkedList()
    assert len(LL) == 0
    assert LL.isEmpty()
    assert str(LL) == "[]"
    print(LL)

    # Test prepend method
    print("\nTesting prepend() for items -A, -B, -C...")
    LL.prepend("-A")
    LL.prepend("-B")
    LL.prepend("-C")
    assert len(LL) == 3
    assert str(LL) == "[-C, -B, -A]"
    print(LL)

    # Test append method
    print("\nTesting append() for items A, B, C...")
    LL.append("A")
    LL.append("B")
    LL.append("C")
    assert str(LL) == "[-C, -B, -A, A, B, C]"
    assert len(LL) == 6
    print(LL)

    # Test insert method
    print("\nTesting insert() for indices: items -- 3: \"0\", 5: B, 8: D...")
    LL.insert(3, "0")
    LL.insert(5, "B")
    LL.insert(8, "D")
    assert str(LL) == "[-C, -B, -A, 0, A, B, B, C, D]"
    assert len(LL) == 9
    print(LL)

    # Test count method
    print("\nTesting count() for items \"0\", B, \":)\"...")
    print(LL)

    print("0 count: " + str(LL.count("0")))
    assert LL.count("0") == 1

    print("B count: " + str(LL.count("B")))
    assert LL.count("B") == 2

    print(":) count: " + str(LL.count(":)")))
    assert LL.count(":)") == 0

    # Test index method
    print("\nTesting index() for items -C, B, \":(\"...")
    print(LL)

    print("-C index: " + str(LL.index("-C")))
    assert LL.index("-C") == 0

    print("B index: " + str(LL.index("B")))
    assert LL.index("B") == 5

    print(":( index: " + str(LL.index(":(")))
    assert LL.index(":(") == -1

    # Test pop method
    print("\nTesting pop() for indices 6, 0, 10...")
    print(LL)

    pop1 = LL.pop(6)
    print("6 pop: " + pop1)
    assert pop1 == "B"

    pop2 = LL.pop(0)
    print("0 pop: " + pop2)
    assert pop2 == "-C"

    pop3 = LL.pop(10)
    print("10 pop: " + str(pop3))
    assert pop3 == None

    assert str(LL) == "[-B, -A, 0, A, B, C, D]"
    assert len(LL) == 7
    print(LL)

    # Test deleteHead and deleteTail methods
    print("\nTesting deleteHead() and deleteTail()...")
    head = LL.deleteHead()
    print("Head: " + head)
    assert head == "-B"

    tail = LL.deleteTail()
    print("Tail: " + tail)
    assert tail == "D"

    assert str(LL) == "[-A, 0, A, B, C]"
    assert len(LL) == 5
    print(LL)

    # Test remove method
    print("\nTesting remove() for items B, C, \":0\"...")
    LL.remove("B")
    LL.remove("C")
    LL.remove(":0")
    assert str(LL) == "[-A, 0, A]"
    assert len(LL) == 3
    print(LL)

    # Test __contains__ method
    print("\nTesting __contains__ (in) for items \"0\", A, \":$\"...")
    print("Contains 0: " + str("0" in LL))
    assert "0" in LL

    print("Contains A: " + str("A" in LL))
    assert "A" in LL

    print("Contains :$: " + str(":$" in LL))
    assert ":$" not in LL

    # Test __getitem__ method
    print("\nTesting __getitem__ for indices 0, 2, 10...")
    print("0 contains: " + LL[0])
    assert LL[0] == "-A"

    print("2 contains: " + LL[2])
    assert LL[2] == "A"

    print("10 contains: " + str(LL[10]))
    assert LL[10] == None

    # Test __setitem__ method
    print("\nTesting __setitem__ for indices: items -- 1: A, 2: B, 10: D...")
    LL[1] = "A"
    LL[2] = "B"
    LL[10] = "D"
    assert str(LL) == "[-A, A, B]"
    print(LL)

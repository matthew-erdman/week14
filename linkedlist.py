from node import *

class LinkedList(object):

    def __init__(self):
        """ construct an empty linked list """
        self.head = None
        self.tail = None
        self.size = 0
        self.isEmpty = True

    def __str__(self):
        """ return string representation of linked list """
        s = "head-->"
        curr = self.head
        for i in range(self.size):
            s += ("(%s)" % str(curr.getItem()))
            curr = curr.getNext()
        s +=("<--tail")
        return s

    def __len__(self):
        """ return length of linked list """
        return self.size

    def append(self, item):
        """ take a string and add it as an element to the end of the linked list """
        new = Node(item)
        if self.isEmpty:
            self.isEmpty = False
            self.head = new
        else:
            self.tail.setNext(new)
        self.tail = new
        self.size += 1

    def prepend(self, item):
        """ take a string and add it as an element to the start of the linked list """
        new = Node(item)
        new.setNext(self.head)
        self.head = new
        if self.isEmpty:
            self.isEmpty = False
            self.tail = new
        self.size += 1

    def deleteHead(self):
        """ delete the first element of the linked list, returning the item it contained """
        oldHead = self.head
        if self.size > 1:
            self.head = self.head.getNext()
        elif self.size == 1:
            self.head = None
            self.tail = None

        if not self.isEmpty:
            self.size -= 1
            if self.size == 0:
                self.isEmpty = True
            return oldHead.getItem()
        return None

    def deleteTail(self):
        """ delete the last element of the linked list, returning the item it contained """
        oldTail = self.tail
        if self.size > 1:
            prev = self.head
            last = self.head.getNext()
            for i in range(self.size-2):
                prev = last
                last = last.getNext()
            self.tail = prev
        elif self.size == 1:
            self.head = None
            self.tail = None

        if not self.isEmpty:
            self.size -= 1
            if self.size == 0:
                self.isEmpty = True
            return oldTail.getItem()
        return None

    def count(self, item):
        """ return the number of occurrences of a given item in the linked list """
        n = self.head
        count = 0
        for i in range(self.size-1):
            if n.getItem() == item:
                count += 1
            n = n.getNext()
        return count

    def index(self, item):
        """ return the index of the first occurrence of a given item in the linked list """
        n = self.head
        for index in range(self.size-1):
            if n.getItem() == item:
                return index
            n = n.getNext()
        return -1

    def insert(self, index, item):
        """ insert a given string as an element at a given index in the linked list """
        if 0 <= index <= self.size-1:
            if index == 0:
                self.prepend(item)
            elif index == self.size-1:
                self.append(item)
            else:
                n = self.head
                for i in range(index-1):
                    n = n.getNext()
                new = Node(item)
                new.setNext(n.getNext())
                n.setNext(new)
                self.size += 1
            if self.isEmpty:
                self.isEmpty = False

    def pop(self, index):
        """ return the item at a given index, removing the element """
        item = None
        if 0 <= index <= self.size-1:
            if index == 0:
                item = self.deleteHead()
            elif index == self.size-1:
                item = self.deleteTail()
            else:
                prev = self.head
                n = self.head.getNext()
                for i in range(index-1):
                    prev = n
                    n = n.getNext()
                item = n.getItem()
                prev.setNext(n.getNext())
                self.size -= 1
                if self.size == 0:
                    self.isEmpty = True
        return item

    def remove(self, item):
        """ remove the first occurrence of a given item in the linked list """
        self.pop(self.index(item))


if __name__ == "__main__":
    # Test linked list initialization
    print("Testing initialization...")
    LL = LinkedList()
    assert len(LL) == 0
    assert str(LL) == "head--><--tail"
    print(LL)

    # Test prepend method
    print("\nTesting prepend() for items -A, -B, -C...")
    LL.prepend("-A")
    LL.prepend("-B")
    LL.prepend("-C")
    assert len(LL) == 3
    assert str(LL) == "head-->(-C)(-B)(-A)<--tail"
    print(LL)

    # Test append method
    print("\nTesting append() for items A, B, C...")
    LL.append("A")
    LL.append("B")
    LL.append("C")
    assert str(LL) == "head-->(-C)(-B)(-A)(A)(B)(C)<--tail"
    assert len(LL) == 6
    print(LL)

    # Test insert method
    print("\nTesting insert() for indices: items -- 3: \"0\", 5: B, 7: D...")
    LL.insert(3, "0")
    LL.insert(5, "B")
    LL.insert(7, "D")
    assert str(LL) == "head-->(-C)(-B)(-A)(0)(A)(B)(B)(C)(D)<--tail"
    assert len(LL) == 9
    print(LL)

    # Test count method
    print("\nTesting count() for items \"0\", B, \":)\"...")
    print("0 count: " + str(LL.count("0")))
    assert LL.count("0") == 1

    print("B count: " + str(LL.count("B")))
    assert LL.count("B") == 2

    print(":) count: " + str(LL.count(":)")))
    assert LL.count(":)") == 0

    # Test index method
    print("\nTesting index() for items B, \":(\"...")
    print("B index: " + str(LL.index("B")))
    assert LL.index("B") == 5

    print(":( index: " + str(LL.index(":(")))
    assert LL.index(":(") == -1

    # Test pop method
    print("\nTesting pop() for indices 6, 0, 10...")
    pop1 = LL.pop(6)
    print("6 pop: " + pop1)
    assert pop1 == "B"

    pop2 = LL.pop(0)
    print("0 pop: " + pop2)
    assert pop2 == "-C"

    pop3 = LL.pop(10)
    print("10 pop: " + str(pop3))
    assert pop3 == None

    assert str(LL) == "head-->(-B)(-A)(0)(A)(B)(C)(D)<--tail"
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

    assert str(LL) == "head-->(-A)(0)(A)(B)(C)<--tail"
    assert len(LL) == 5
    print(LL)

    # Test remove method
    print("\nTesting remove() for items C, B, \":0\"...")
    LL.remove("C")
    LL.remove("B")
    LL.remove(":0")
    assert str(LL) == "head-->(-A)(0)(A)<--tail"
    assert len(LL) == 3
    print(LL)

    print("\nDone! Final list:")
    print(LL)

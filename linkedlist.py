from node import *

class LinkedList(object):

    def __init__(self):
        """ construct an empty linked list """
        self.head = None
        self.tail = None
        self.size = 0

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
        n = Node(item)
        if self.size == 0:
            self.head = n
        else:
            self.tail.setNext(n)
        self.tail = n
        self.size += 1

    def prepend(self, item):
        n = Node(item)
        n.setNext(self.head)
        self.head = n
        if self.size == 0:
            self.tail = n
        self.size += 1

    def deleteHead(self):
        oldHead = self.head
        if self.size > 1:
            self.head = self.head.getNext()
        elif self.size == 1:
            self.head = None
            self.tail = None

        if self.size > 0:
            self.size -= 1
            return oldHead.getItem()
        return None

    def deleteTail(self):
        oldTail = self.tail
        if self.size > 1:
            secondToLast = self.head
            last = self.head.getNext()
            while last.getNext() != None:
                secondToLast = last
                last = last.getNext()
            self.tail = secondToLast
        elif self.size == 1:
            self.head = None
            self.tail = None

        if self.size > 0:
            self.size -= 1
            return oldTail.getItem()
        return None

    def count(self, item):
        count = 0
        n = self.head
        while n != None:
            if n.getItem() == item:
                count += 1
            n = n.getNext()
        return count

    def index(self, item):
        index = 0
        n = self.head
        while n != None:
            if n.getItem() == item:
                return index
            n = n.getNext()
            index += 1
        return -1

    def insert(self, index, item):
        new = Node(item)
        if index <= size-1:
            if index == 0:
                self.prepend(item)
            elif index == size-1:
                self.append(item)
            else:
                n = self.head
                for i in range(index-1):
                    n = n.getNext()
                new.setNext(n.getNext())
                n.setNext(new)
            self.size += 1
        else:
            print("Index OOB")


if __name__ == "__main__":		   # test the following methods: init, str, append, len
    LL = LinkedList()
    assert len(LL) == 0
    assert str(LL) == "head--><--tail"
    LL.prepend("-A")
    LL.prepend("-B")
    LL.prepend("-C")
    assert len(LL) == 3
    assert str(LL) == "head-->(-C)(-B)(-A)<--tail"
    LL.append("A")
    LL.append("B")
    LL.append("C")
    assert str(LL) == "head-->(-C)(-B)(-A)(A)(B)(C)<--tail"
    assert len(LL) == 6
    LL.deleteHead()
    LL.deleteTail()
    assert str(LL) == "head-->(-B)(-A)(A)(B)<--tail"
    assert len(LL) == 4
    print(LL)

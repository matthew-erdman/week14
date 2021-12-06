"""
    Description: Node class, where each node has two instance variables: one to hold
    the node data, and one to hold a pointer to another node. Used to build a linked list.
    Author: Matthew Erdman
    Date: 11/18/21
"""

class Node(object):
    """ class for a single Node object, contains string data and pointer to next node """
    def __init__(self, item):
        """ construct new node with given item, next node initially set to None """
        self.item = item
        self.next = None

    def __str__(self):
        """ return a string representation of the node """
        s = "(%s)" % str(self.item)
        if self.next == None:
            s += "--|"
        else:
            s += "-->"
        return s

    def getItem(self):
        """ return the item contained in the node """
        return self.item

    def getNext(self):
        """ return the next node """
        return self.next

    def setItem(self, i):
        """ set node item to i """
        self.item = i

    def setNext(self, n):
        """ set node next to n """
        self.next = n


if __name__ == "__main__":              # test init, str, setNext, setItem
    n1 = Node("jeff")
    n2 = Node("zach")
    n3 = Node("lauri")
    n4 = Node("rich")

    n1.setNext(n2)
    print(n1)
    n2.setNext(n3)
    print(n2)
    n3.setNext(n4)
    print(n3)
    n3.setItem("julie")
    # print entire linked list to confirm it looks okay
    print("%s%s%s%s" % (str(n1), str(n2), str(n3), str(n4)))

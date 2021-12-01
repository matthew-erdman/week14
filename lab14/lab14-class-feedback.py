"""
    Lab 14 - Linked Lists - Code Revision Activity

    Mr. Bloom's feedback + suggestions for each component of the grading rubric:

    *  SOLUTION  *  MODULAR DESIGN  *  CODE READABILITY  *  USER INTERFACE  *
"""


############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
####################################################################                    ####################################################################
####################################################################      SOLUTION      ####################################################################
####################################################################                    ####################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################


""" ####################################################################################
    ############################  Works for all test data  #############################
    ####################################################################################

    Read the lab handout and class notes more carefully!
        - What should your function return if the list it is passed is empty?
        - What should your function return if you're deleting something from the list?
        - What should you do if you're asked to index a list at a position that doesn't exist?
        - What should you do if the list only has 1 item in it and you're asked to delete that item?
        - etc... etc...

    NOTE: In the class notes (Lesson 14.3) on page 1, I provide instructions on what to do
    if deleteHead/Tail is passed an empty list. Heed those instructions. Also, when I say
    'None', I don't mean 'nothing'. I mean python's built-in constant, the None type.
    If you don't know what that is or what I mean by this, read up on it in the python docs:

            https://docs.python.org/3/library/constants.html#None

    (I know functions without 'return' statements return 'None' by default but that does
    not mean you should leave the return statement blank. return this constant explicitly.
    It tells the user/programmer something really important about their function call;
    it's an intentional design choice that improves legibility).
"""


############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
####################################################################                    ####################################################################
####################################################################   MODULAR DESIGN   ####################################################################
####################################################################                    ####################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################


"""
    ####################################################################################
    ##########################  optimal branching patterns  ############################
    ####################################################################################

    You're trying to design the optimal branching pattern, one without unnecessary branches
    but one with enough branches, in order to cover all of the weird, edge cases (# of
    edge cases vary depending upon the situation/function, but there are usually 2-4).
    The lab handout and class notes discuss this in greater detail, as well as some of the
    edge cases you should account for. Some edge cases that you need to account for in
    your code are not explicitly mentioned in the lab handout or class notes. These edge
    cases are ones that you should already know how to account for and respond to.

    Here's a freebie edge case hint -- this is not mentioned in the lab handout or notes
    but should be something you've coded for in your solution to the .index() function --
    What should the function do in the event that .index() executes doesn't find the item
    it's looking for in the list?  HINT: take a look at your binary and linear search
    code from Soft Dev -- you probably have it in your Week 1 folders from this year,
    when we studied sorting algorithms.

    Another thing to look out for in your design of your branching patterns are the "exit"
    points. Ideally, functions will only have one exit point -- one line of code that
    terminates the function and returns to wherever the function was originally called
    cfrom in the program. So, with that in mind, use 'return' statements sparingly --
    shoot for just one 'return' statement at the end of the function.

    Along the same lines, try not to update the size of the list in 3-4 different places
    within a single function. Shoot for 1-2x. Plus, in terms of the overall design of
    the algorithm, where does the list-size update code really belong??
    The IF statements are there to help us identify edge cases and respond to them, and
    incrementing/decrementing the size of the list doesn't really have anything to do
    with edge cases. For example, if we're removing an item from the list, we subtract
    one regardless of the situation, whether there is 1 item in the list or 20 items.

    EXAMPLE OF WHAT NOT TO DO:

            def append(self, item):
                n = Node(item)
                if self.size == 0:
                    ____________
                    ____________
                    self.size += 1
                elif self.size == 1:
                    ____________
                    ____________
                    self.size += 1
                else:
                    ____________
                    ____________
                    ____________
                    self.size += 1

    How could we simplify this branching pattern?  Can we move the line of code,
    self.size += 1, somewhere else in the sequence so we don't need to keep rewriting it?

    The reason I said to repeat the self.head/tail stuff occasionally was to make it clear
    which node pointers were being modified/set when we have empty lists vs. one-item lists.
    The self.size += 1 stuff is kind of unrelated to the actual list traversal and list
    operations, though. Besides, there will never be an instance where we delete something
    and don't subtract 1 and update the size/len of the list. We must always keep an
    accurate account of the number of items in the list, otherwise our code becomes unusable
    even if the self.size count is off by just a single item.


    ####################################################################################
    ##############################  designing functions  ###############################
    ####################################################################################

    All functions (except for main()) should have a 'return' statement. Obviously not all
    functions return values, as is the case with the append() method, but we should still
    write 'return' at the end of the function. This helps with program legibility by
    explicitly stating that this function does not return anything, which is helpful when
    we're writing function calls because we need to know whether we're supposed to assign
    the function call to a variable, so it can save the return value later on when the
    function is finished executing.

    tl;dr  You should always have a 'return' statement at the end of your function defintions
           It might not always have a variable or value next to it that it's returning, but
           that's okay.

    EXAMPLE:
                def append(self, item):
                    n = Node(item)
                    if self.size == 0:
                        __________
                        __________
                    else:
                        __________
                        __________
                    self.size += 1
                    return


    ####################################################################################
    ###########################  function def/param/return  ############################
    ####################################################################################

    When you define common functions like .index() and .remove() and .count() -- methods
    that are standard across data structures and programming languages -- you should
    mimic their function definiton (i.e., the number of params, the names of the params,
    and the order in which the params are passed to the function).

    The .index() function, for example, is the same in all languages. You pass it one
    parameter (the item you want to search for, usually referred to as an 'element') and
    it returns the index (position) of the first occurence of that element in the list
    (or, if the item is not found in the list at any position, -1 is returned.)

    Here's the function comment for the .indexOf() method in Java's ArrayList class:

        ----------------------------------------------------------------------------------------
        --------------------------  Java.util.Arraylist.indexOf()  -----------------------------
        ----------------------------------------------------------------------------------------
        Description  : The java.util.ArrayList.indexOf(Object) method returns the index of the
                       first occurrence of the specified element in this list, or -1 if this
                       list does not contain the element.

        Declaration  : Following is the declaration for java.util.ArrayList.indexOf() method
                       public int indexOf(Object o)

        Parameters   : Object o − The element to search for.

        Return Value : This method returns the index of the first occurrence of the specified
                       element in this list, or -1 if this list does not contain the element.
        ---------------------------------------------------------------------------------------

        Check out the documentation for yourself:
            PYTHON -- https://www.programiz.com/python-programming/methods/list/index
              JAVA -- https://www.tutorialspoint.com/java/util/arraylist_indexof.htm
                JS -- https://www.w3schools.com/jsref/jsref_indexof.asp
               C++ -- https://www.cplusplus.com/reference/algorithm/find/
             Swift -- https://developer.apple.com/documentation/foundation/nsarray/1417076-index
              Ruby -- https://ruby-doc.org/core-2.7.0/Array.html#method-i-index


    ####################################################################################
    #######################          code redundancies         #########################
    ####################################################################################

    No redundancies within functions unless it's one of those few instances where it
    improves code legibility. Remember, if a line of code appears in all of the branches,
    then it can be deleted from each one and written once at the beginning/end of the
    branching pattern (outside of it so it will be run no matter which branch executed).

    Look carefully for these^ redundancies. The code within each branch may look different
    but be doing the exact same thing, depending upon how consistent you are with your
    variable naming conventions.

    One of the methods you're supposed to write is entirely redundant and can simply call
    other methods you've written to accomplish the task. I mention this in the notes and
    lab handout and that you should not reinvent the wheel here -- just outsource the work
    to your previously written methods. A lot of the implementations I've seen are overkill.

    Also, if you've chosen to write the isEmpty() method, you should use it wherever you
    have an 'if self.size == 0:'

    ####################################################################################
    ########################          task delegation         ##########################
    ####################################################################################

    Avoid rewriting the same code -- delegate list operations/tasks to
    functions you've already written where/when possible. The lab handout and class notes
    talk about this for a few of the functions, but there are a few other opportunities
    to reuse methods you've previously written (or will be writing shortly). HINT: look
    what the instructions say for the .remove() method -- it's a SUPER easy implementation
    that should take you all of 30 seconds to write, yet some of the .remove() functions
    I've seen are 15-25 lines of code when you should have just 3 lines of code.

    ####################################################################################
    ######################  list traversal vs. list operation   ########################
    ####################################################################################

    Navigate to a specific position in the list with a targeted range() function.
    Better design than the alternative, which is the list operation being performed
    during a traversal, and it's more efficient without conditional checks (IF statements).
    This is what we talked about during our last class before the break. Keep traversal and
    and any operations performed separate from one another in your code.
"""


############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
####################################################################                    ####################################################################
####################################################################  CODE READABILITY  ####################################################################
####################################################################                    ####################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################


""" ####################################################################################
    ################################  INLINE COMMENTS  #################################
    ####################################################################################

    One other thing I noticed is that you hardly have ANY inline comments.
    You don't need many because the functions are short, but it's a bit hard/dense to read
    this program without any inline comments. You don't need to torture yourself writing them either.
    After you've commented, say, the traversal of the linked list to a particular index, you don't
    need to write comments for it again. For example, the first time you need to do a list traversal
    (if we're reading your code from top to bottom) is when you get to the deleteTail() function.
    So, for this one, you could write inline comments explaining how it works with a linked list
    when you want to access a certain item (reach a certain position) in the list. Here's how
    I commented mine in deleteTail().

    ############
    curr = self.head                # Start at the beginning of the linked list
    for i in range(index-1):        # Traverse from node to node until reach index-1
        curr = curr.getNext()       # 'curr' will store the item at index-1 when 'for' loop ends
    prevNode = curr                 # This node will be positioned right before our new node
    nextNode = prevNode.getNext()   # This node will be positioned right after our new node
    prevNode.setNext(newNode)       # Position new node after node at index-1
    newNode.setNext(nextNode)       # Position next node after new node
    self.size += 1                  # Increment size of the list by 1
    return
    ############

    After that (from then on), whenever I have to do a linked list traversal in a function
    I just write a two-word comment next to the 'for' loop. Like this:

            curr = self.head
            for i in range(index - 1):          # list traversal
                curr = curr.getNext()
            ____Node = curr                     # the prev/next/del/new node

    Then, after the traversal is over, I just rename the variable 'curr' so that it
    it describes which node (position in the list) I stopped on, and then it's clear
    from the comment "list traversal" and the variable "prevNode" that I traversed
    the linked list from the very beginning all the way up to the node BEFORE
    the node I want to insert/delete/change/etc.


    ####################################################################################
    ####################################  IDENTIFIERS  #################################
    ####################################################################################

    Be consistent in how you name variables. In general, there's nothing wrong with the
    names you've chosen to describe the nodes/items/indices, but you're not very consistent
    in your naming practices. For instance, in your list traversal code that appears in a
    number of functions, you start with this line: someVariable = self.head
    The four most common names were 'node', 'n', 'curr', and 'currNode'. All of these names are
    great, but commit to one of them and use the same name for that variable, every time
    it appears in a function.

    What you should also do is let that name dictate how you name related data. For instance,
    if I chose to name my self.head reference 'currNode', then I should use names like 'prevNode'
    and 'nextNode' and 'newNode' to describe related data. Here are some name "collections" that
    work well together:
                             curr    /      prev      /     next     /  new
                          currNode   /    prevNode    /   nextNode   /  newNode
                        currentNode  /  previousNode  /   nextNode   /  newNode

    Another variable name to decide on from the beginning is 'index'. Are you going to
    call it:
                            index / idx / i / pos
    What about items in the list? Will you refer to each member of a list as an 'item' or an 'element' or an 'elem'?

    etc... etc...

    tldr: choose a variable name and stick to it!


    ####################################################################################
    ################################  PROGRAMMING STYLE  ###############################
    ################################    & CONVENTIONS    ###############################
    ####################################################################################

    ##################################  80 char limit  #################################
    Watch the 80 character limit. If you don't have a grey line denoting the 80 char limit,
    go to File>Preferences in Atom (or any text editor) and find the "Editor" settings.
    In the 'Editor' section/tab, find the "Preferred Line Length" setting and make sure it's set to 80

    ####################################  whitespace  ##################################
    Use blank lines to separate functions from one another but, in general, don't use blank lines to
    separate the code within your functions. Your functions are (or should be) short enough in length
    that it's still easy to read when all the lines are touching each other. Think of a function
    like a paragraph.

    ####################################  var. names  ##################################
    camelCase or snake_case -- either is fine.  BUT! You must choose one and stick to it
    throughout the entire program. Do not flip back and forth between the two styles.

    Boolean flags are written in ALL CAPS and phrased like a question. Here are
    some examples:
                    "Is player the winner?"         IS_WINNER
                    "Is the game over?"             IS_GAMEOVER
                    "Is the number even?"           IS_EVEN
                    "Is the number odd?"            IS_ODD
                    "Is it alphabetic chars?"       IS_ALPHA
                    "Is it only numeric chars?"     IS_NUMERIC
                    "Is the user online?"           IS_ONLINE
                    "Is the item in the list?"      IS_IN_LIST
                    "Is the list empty?"            IS_EMPTY
                    "Is user logged in?"            IS_LOGGED_IN
"""


############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
####################################################################                    ####################################################################
####################################################################   USER INTERFACE   ####################################################################
####################################################################                    ####################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################


"""
    ####################################################################################
    ####################################  TEST CODE  #################################
    ####################################################################################

    Remember, this program was written for another python programmer. You made a class
    for a singly-linked list data structure and it will be imported into future programs
    when it would be advantageous to use a Linked List to store your data. For this to be
    worthwhile, the data structure must work as well as (in not better than) one of Python's
    built-in data structures, like a List or Dictionary. In other words, it must be able
    to do all of the normal functions data structures need to do, like inserting/removing/
    finding/counting/changing/etc... and it must be able to perform all of these manipulations
    reliably, no matter the size of the list or where the item is being inserted/deleted.

    Therefore, I, the programmer who wants to use your LinkedList.py class file in my own
    personal program, need to know that your data structure works all of the time. To convince
    me of that, tell me about the tests you've included in your main() function and print the
    list often so I can visually verify that the operations are being performed as expected.

    Be sure to test your edge cases and your normal/usual case for each function to ensure it's working properly.
    In general, most of you need to have a lot more test code. And, I'm not saying this simply
    because it's helpful for people who want to use your Class code or because I, personally, want to
    see it in your programs.  You need more test code because your programs are crashing (or yielding unexpected
    results) when I run your functions on the "edge cases", like when...
        ... the list is empty
        ... you're deleting the last item in a list
        ... the item you were searching for was not found
        ... you're inserting an item at the very end of a list
        ... etc...

    In general, most of you need a lot more test code. If, for instance, your pop() function has three branches
    (if/elif/else), then you should probably test the functionality of pop() in each branch/scenario. Let's take
    a look at an example. Here's what my test code looks like for the pop() method:

            print("\n--------------------------------------------------------")
            print("--------------------  testing pop()  -------------------")
            print("--------------------------------------------------------")

            print("\t       TEST :  removing first item in the list")          # test 1
            print("\tlist before : ", LL)
            removedItem = LL.pop(0)
            print("\t list after : ", LL)
            print("\t    deleted : ", removedItem)

            print()                                                            # test 2
            print("\t       TEST :  removing last item in the list")
            print("\tlist before : ", LL)
            removedItem = LL.pop(len(LL)-1)
            print("\t list after : ", LL)
            print("\t    deleted : ", removedItem)

            print()                                                            # test 3
            print("\t       TEST :  removing item at index", int(len(LL)/2))
            print("\tlist before : ", LL)
            removedItem = LL.pop(int(len(LL)/2))
            print("\t list after : ", LL)
            print("\t    deleted : ", removedItem)

            print("\n-----------------  done testing pop()  -----------------\n")

    And, for comparison, here's what I'm seeing in most of your programs:

            assert str(LL) == "head-->(2)(2)(3)(3)(4)(A)(B)<--tail"
            assert LL.pop(1) == "2"
            assert str(LL) == "head-->(2)(3)(3)(4)(A)(B)<--tail"

    A single test. Perhaps you had more before and only deleted it after you got it
    working, but I'm not inclined to think that's the case for most of you. It's not
    personal or a judgement on my part--it's that I've tested your programs and they're
    frequently crashing on the edge cases, where you pop(0) (remove the first item in
    the list). Or, perhaps that works just fine but when you pop(0) and the list only
    has one item in it, then it breaks. Or, perhaps your pop() method usually works
    but occasionally (in certain edge cases) doesn't return a value and that causes
    the program to crash, bec/ we end up with the None type stored in a variable when
    we were under the impression that variable was holding the item that was removed
    from the list. I'm seeing all of these issues and so, I suspect, you ran out of
    time and, with extra time, could do a more thorough job of testing your code to
    ensure it works for all test data and is visible and helpful for the user.
"""

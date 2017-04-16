
from salboard import SALboard
from salbnode import SALBnode


def salb2salbLL(salb):
        
        
        
        head = SALBnode()
        tail = SALBnode()
        head.next = tail
        count_squares = salb.numSquares
        count_squares = count_squares - 2
        
        source = []
        destination = []
        
        for i in salb.snadders.keys():
                source.append(i)
                destination.append(salb.snadders[i])        
        
        
        while count_squares != 0:
                temp = SALBnode(head)
                #temp.next = head
                head = temp
                count_squares = count_squares -1
                
        tail.next = head
        
        count_snader = 0
        done = False
        current = head
        previous = None
        
        
        while not done:
                count_snader = count_snader + 1
                
                if len(source) == 0 and len(destination) == 0:
                        done = True
                else:
                        if source[-1] < destination[-1] and source[-1] == count_snader:
                                previous = current
                                while destination[-1] != count_snader:
                                        current = current.next
                                        count_snader = count_snader + 1
                                previous.snadder = current
                                source.pop()
                                destination.pop()                                
                        
                        elif source[-1] > destination[-1] and destination[-1] == count_snader:
                                previous = current
                                while source[-1] != count_snader:
                                        current = current.next
                                        count_snader = count_snader + 1
                                current.snadder = previous
                                source.pop()
                                destination.pop()
                
                current = current.next 
       
                                
        return head 



    
    
    
if __name__ == "__main__":
        import math
        import doctest
        # first run doctest
        doctest.testmod()
    
        # sample board
        __salb1__ = SALboard(25, {2: 10, 24: 14})
        # first node is the output of the salb2salbLL function
        __head__ = salb2salbLL(__salb1__)
        # get the max width by rounding down the square root of numSquares
        __maxwidth__ = math.floor(math.sqrt(__salb1__.numSquares))
    
        try:
            # copy the nodes into a list
            __squares__ = []
            # set node to be the head of the list
            __node__ = __head__
            # for every node
            for o in range(0, __salb1__.numSquares):
                # append it to the list
                __squares__.append(__node__)
                # move one forward
                if __node__.next is not None:
                    __node__ = __node__.next
                else:
                    print("Null pointer at node.next\n One of your links is not",
                          "pointing to the right place :O")
            # empty start:end dict
            __snadders__ = {}
            # run through the list and copy the start:end pairs from the nodes
            for p in range(0, len(__squares__)):
                if __squares__[p].snadder is not None:
                    __snadders__[p + 1] = __squares__.index(
                        __squares__[p].snadder) + 1
            # keep records of the start and end of each snadder from the dict
            __start__ = list(__snadders__.keys())
            __end__ = list(__snadders__.values())
    
        except (IndexError, TypeError) as ex:
            print(
                "Oh no! Something broke, double check your code!")
        else:
            if list(__snadders__.keys()) != __start__:
                print("Your linked list snadders and your dictionary snadders",
                      "don't match 0_0\n")
    
        # counter to reference the current square's number
        __counter__ = 1
        try:
            # for each row in the board
            for k in range(0, int(math.ceil(__salb1__.numSquares / __maxwidth__))):
                # make a string to add the squares into
                row = ""
                # for each column in the board
                for j in range(int(k * __maxwidth__), int((k + 1) * __maxwidth__)):
                    # if the square has a snadder
                    if __counter__ in __start__:
                        # print a square with the number of the index in it
                        row += ("[_" + str(__start__.index(__counter__)) + "S_]")
                    elif __counter__ in __end__:
                        # print a square with the number of the index in it
                        row += ("[_" + str(__end__.index(__counter__)) + "E_]")
                    elif __counter__ <= __salb1__.numSquares:
                        # print an empty square
                        row += ("[____]")
                    # add one to the counter
                    __counter__ += 1
                    # move to the next node
                    __node__ = __node__.next
                # print the row
                print(row, "\n\n")
        except IndexError:
            print("Graph failed :(\nDouble check your code!")


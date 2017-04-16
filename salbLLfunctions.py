"""
# Copyright Nick Cheng, 2016, Greg (Hidayat) Mehdiyev
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSCA48, Winter 2017
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""

from salboard import SALboard
from salbnode import SALBnode

# Add your functions here.
'''
take a dictionary reprensentation of a snadder board,
and return a linked list representation of the same board
'''
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
        # temp.next = head
        head = temp
        count_squares = count_squares - 1

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
        if salb.numSquares == count_snader:# in case of 'count_snader' bigger than square number
            count_snader = 0

    return head
'''
take a linked list representation of a snadder board and a step size,
return whether a player playing on the board with the given step size will ever
land on the last square.
'''
def willfinish(first, stepsize):
    snadder_num = 0#number of snadders
    current = first
    while (current.next != first):
        if current.snadder is not None:
            snadder_num += 1
        current = current.next
    current = first
    count_snadder = 0#count snadder landing on
    #first step
    for i in range(stepsize - 1):
        current = current.next
    #if first step land on snadder,return first square
    if current.snadder is not None:
        count_snadder += 1
        current = first
    while (current.next != first):
        #each step
        for i in range(stepsize):
            current = current.next
        #if landing on snadder source,return snadder destination
        if current.snadder is not None:
            current = current.snadder
            count_snadder += 1
        if current.next == first:#land on the last square,win
            return True
        if count_snadder > snadder_num:#if land on same snadder twice,loop
            return False

'''
take a linked list representation of a snadder board and two stepsizes for players 1
and 2 respectively,and return the number of players who win the game
'''
def whowins(first, step1, step2):
    play1 = willfinish(first, step1)#whether to win
    play2 = willfinish(first, step2)
    if play1 and play2:#both player 1 and player 2 can win
        current_1 = first
        #processing first step
        for i in range(step1 - 1):
            current_1 = current_1.next
        if current_1.snadder is not None:
            current_1 = first
        current_2 = first
        for i in range(step2 - 1):
            current_2 = current_2.next
        if current_2.snadder is not None:
            current_2 = first
        while (True):
            for i in range(step1):
                current_1 = current_1.next
            if current_1.snadder is not None:
                current_1 = current_1.snadder
            #player 1 lands on last square,win
            if current_1.next == first:
                return 1
            for i in range(step2):
                current_2 = current_2.next
            if current_2.snadder is not None:
                current_2 = current_2.snadder
            # player 2 lands on last square,win
            if current_2.next == first:
                return 2
    elif play1 and not play2:#player1 can win and player 2 can't win
        return 1
    else:#no one can win
        return 2

'''
take a linked list representation of the snadder board
and return a linked list that represents its dual
'''
def dualboard(first):
    current = first
    while (current.next != first):#while not the
        #interchanged,just make the snadder none
        if current.snadder is not None and current.snadder.snadder is not None:
            before = first
            while (True):
                if before == current.snadder:#find current square snadder
                    before.snadder = None
                    break
                before = before.next
        else:
            #not interchanged,process snadder
            if current.snadder is not None:
                after = current.next#search the after squares
                while(True):
                    if after == current.snadder:#find destination,make it source
                        after.snadder = current
                        break
                    if after.next == first:#not find destination,make snadder source and current snadder none
                        current.snadder.snadder = current
                        current.snadder = None
                        break
                    after = after.next

        current = current.next
    return first



    
    
    # this code tests your salb2salbLL function by printing a visual representation
    # of your game board! Look at the example in the piazza post to see what it
    # should look like
if __name__ == "__main__":
        import math
        import doctest
        # first run doctest
        doctest.testmod()
    
        # sample board
        __salb1__ = SALboard(25, {2: 10, 24: 14})
        # first node is the output of the salb2salbLL function
        __head__ = salb2salbLL(__salb1__)
        #__head__ = dualboard(__head__)
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


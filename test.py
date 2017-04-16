class SALBnode:
    """Node for linked list representation of snakes and ladders board."""
    def __init__(self, next= None,snadder= None):
        # Representation invariant:
        #  self.next points to the next SALBnode.
        #  If self.snadder!=None, then self is the source of a snadder
        #   whose desination is self.snadder.
        #  If self.snadder==None, then self is not the source of a snadder.
        self.next = next
        self.snadder = snadder


if __name__ == '__main__':
    
    head = SALBnode()
    tail = SALBnode()
    head.next = tail
    count_squares = 20
    count_squares = count_squares - 2    
    
    while count_squares != 0:
            temp = SALBnode()
            temp.next = head
            head = temp
            count_squares = count_squares -1
            
    count = 0
    tail.next = head
    curr = head.next
    while curr != head:
        count = count + 1
        curr = curr.next
        
    print (count)
    
    
    
    

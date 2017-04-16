

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

def willfinish(first, stepsize):
        
        return
    
if __name__ == '__main__':
        import time
    
        # edit these three things
        snadders = {6:9,543:921}
        tiles=10000
        step_size = 2
        
        start=time.time()
        long_board = salb2salbLL(SALboard(tiles, snadders))
        can=willfinish(long_board, step_size)
        print('User can finish: ' + str(can))
        end=time.time()
        print('Took {} seconds to check if a board with {} tiles and {} snadders is winnable'.format(end-start,tiles,len(snadders.keys())))

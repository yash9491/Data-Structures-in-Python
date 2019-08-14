from DLLNode import Node

class InsertIntoDLL:

    def __init__(self):
        self.start = None

    def InserAtEnd(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
            return
        else:
            temp = self.start
            while(temp.next):
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def InsertAtBegin(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
            return
        else:
            new_node.next = self.start
            self.start.prev = new_node
            self.start = new_node
    
    def printdll(self):
        temp = self.start
        while(temp):
            print(temp.data)
            temp = temp.next

    def printreversedll(self):
        temp = self.start
        while temp.next is not None:
            temp = temp.next
        
        while(temp != self.start):
            print(temp.data)
            temp = temp.prev
        print(self.start.data)

    def InsertAtGivenPosition(self, pos, data):
        new_node = Node(data)
        if(pos == 0):
            self.InsertAtBegin(data)
        else:
            current = self.start
            previous = None
            current_position = 0
            while(current_position < pos):
                previous = current
                current = current.next
                current_position += 1
            new_node.next = current
            previous.next = new_node
            new_node.prev = previous
            current.prev = new_node
        
if __name__ == '__main__':
    
    dll = InsertIntoDLL()

    print('Inserting Data at End into DLL')
    dll.InserAtEnd(11)
    dll.InserAtEnd(12)
    dll.InserAtEnd(13)
    dll.InserAtEnd(14)
    print('Printing Data in DLL')
    dll.printdll()

    print('Inserting Data at Begin into DLL')
    dll.InsertAtBegin(21)
    dll.InsertAtBegin(22)
    print('Printing Data in DLL')
    dll.printdll()

    print('Inserting Data at Begin into DLL')
    dll.InsertAtGivenPosition(2,19)
    dll.InsertAtGivenPosition(3,55)
    print('Printing Data in DLL')
    dll.printdll()

    print('Printing Reverse Data/backwards in DLL')
    dll.printreversedll()



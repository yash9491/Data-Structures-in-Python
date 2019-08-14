from DLLNode import Node

class DeleteDLL:

    def __init__(self):
        self.start = None
    
    def DeleteAtEnd(self):
        temp = self.start
        while(temp):
            temp = temp.next
            if(temp.next.next is None):
                temp.next = None
                return
       
    def DeleteAtBegin(self):
        self.start = self.start.next

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
    
    def printdll(self):
        temp = self.start
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__ == '__main__':

    dll = DeleteDLL()

    print('Inserting Data at End into DLL')
    dll.InserAtEnd(11)
    dll.InserAtEnd(12)
    dll.InserAtEnd(13)
    dll.InserAtEnd(14)
    dll.InserAtEnd(15)
    print('Printing Data in DLL')
    dll.printdll()

    print('Deleting Data at Begining into DLL')
    dll.DeleteAtBegin()
    print('Printing Data in DLL')
    dll.printdll()

    print('Deleting Data at End into DLL')
    dll.DeleteAtEnd()
    print('Printing Data in DLL')
    dll.printdll()      
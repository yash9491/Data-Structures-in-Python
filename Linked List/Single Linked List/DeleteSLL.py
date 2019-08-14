from SLLNode import Node

class DeleteSLL:

    def __init__(self):
        self.start = None

    def DeleteFirstNode(self):
        self.start = self.start.next
    
    def DeleteLastNode(self):
        temp = self.start
        while(temp):
            temp = temp.next
            if(temp.next.next is None):
                temp.next = None
                return

    def DeleteAtGivenPosition(self,pos):
        if(pos == 0):
            self.DeleteFirstNode()
        else:
            current = self.start
            previous = None
            current_position = 0
            while(current_position < pos):
                previous = self.start
                current = current.next
                current_position += 1
            previous.next = current.next.next
            current.next = None

    def DeleteDataRecursively(self, data):
        temp = self.start
        current_position = 0
        while(temp):
            if(temp.data == data):
                self.DeleteAtGivenPosition(current_position)
        current_position += 1

    def PrintSLL(self):
        temp = self.start
        while(temp):
            print(temp.data)
            temp = temp.next
    
    def InserAtEnd(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
            return
        last = self.start
        while(last.next):
            last = last.next
        last.next = new_node

if __name__=='__main__':
    
    delsll = DeleteSLL()

    delsll.InserAtEnd(11)
    delsll.InserAtEnd(12)
    delsll.InserAtEnd(13)
    delsll.InserAtEnd(14)
    delsll.InserAtEnd(15)

    print ('Printing Single Lisnked List')
    delsll.PrintSLL()

    print('Deleting the first element from list')
    delsll.DeleteFirstNode()
    print ('Printing Single Lisnked List')
    delsll.PrintSLL()

    print('Deleting the last element from list')
    delsll.DeleteLastNode()
    print ('Printing Single Lisnked List')
    delsll.PrintSLL()
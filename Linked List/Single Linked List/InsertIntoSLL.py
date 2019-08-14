from SLLNode import Node 

class InsertIntoSLL:

    def __init__(self):
        self.start = None

    def InserAtEnd(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
            return
        last = self.start
        while(last.next):
            last = last.next
        last.next = new_node

    def InsertAtBegin(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
            return
        new_node.next = self.start
        self.start = new_node

    def InsertAtGivenPosition(self, pos, data):
        new_node = Node(data)
        if(pos == 0):
            new_node.next = self.start
            self.start = new_node
        else:
            previous = None
            current = self.start
            current_posotion = 0
            while(current_posotion < pos) and current.next:
                previous = current
                current = current.next
                current_posotion += 1
            previous.next = new_node
            new_node.next = current
                
    def PrintSLL(self):
        temp = self.start
        while(temp):
            print (temp.data)
            temp = temp.next

if __name__=='__main__':

    sll = InsertIntoSLL()

    print ('Inserting at the end of Single Lisnked List')
    sll.InserAtEnd(23)
    sll.InserAtEnd(45)
    sll.InserAtEnd(85)
    print ('Printing Single Lisnked List')
    sll.PrintSLL()

    print ('Inserting at the begining of Single Lisnked List')
    sll.InsertAtBegin(11)
    print ('Printing Single Lisnked List')
    sll.PrintSLL()

    print ('Inserting at the given position of Single Lisnked List')
    sll.InsertAtGivenPosition(2,10)
    print ('Printing Single Lisnked List')
    sll.PrintSLL()
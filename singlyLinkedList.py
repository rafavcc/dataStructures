# Create Node
# Node: data + next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


#Create linked list

class LinkedList:
# Only contains a head, which is a node
    def __init__(self):
        self.head = None

# Add nodes to the linked list
    def insert(self, newNode):
        if self.head == None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next == None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

# Print linked list
    def printLinkedList(self):
        if (self.head) is None:
            print("List is empty")
            return
                
        iterador = self.head
        print(iterador.data) 
        iterador = iterador.next

        while (iterador.next != None):
            print(iterador.data)
            iterador = iterador.next
        print(iterador.data)


# First node with name but point to none
firstNode = Node("Rafael")
secondNode = Node("Fernanda")
thirdNode = Node("Ligia")
linkedList = LinkedList()
linkedList.insert(firstNode)
linkedList.insert(secondNode)
linkedList.insert(thirdNode)
linkedList.printLinkedList()
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
            
    def insertAsHead(self, newNode):
        # Store current head temporarily in another structure
        temporaryNode = self.head
        # New Node is the new head
        self.head = newNode
        # New head points to temporary node, the former head
        self.head.next = temporaryNode 
        # Delete temporary node
        del temporaryNode

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

    def insertAt(self, newNode, position):
        # if position == 0:
        #     self.insertAsHeas(newNode)
        # else:
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1
            

# First node with name but point to none
firstNode = Node("One")
secondNode = Node("Two")
thirdNode = Node("Three")
linkedList = LinkedList()
linkedList.insert(firstNode)
linkedList.insert(secondNode)
linkedList.insert(thirdNode)
fourthNode = Node("Zero")
linkedList.insertAsHead(fourthNode)
fifthNode = Node("Zero_point_five")
linkedList.insertAt(fifthNode, 3)
linkedList.printLinkedList()
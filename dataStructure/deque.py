from sys import stdin

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return f"{self.data}"

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def pushfront(self, data):
        newNode = Node(data)

        if self.count == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

        self.count += 1
    
    def pushback(self, data):
        newNode = Node(data)

        if self.count == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        
        self.count += 1

    def popfront(self):
        if self.count == 1:
            temp = self.head

            self.head = None
            self.tail = None
            self.count -= 1
            
            return temp

        elif self.count > 1:
            temp = self.head

            self.head = self.head.next
            self.count -= 1

            return temp

        else:
            return None

    def popback(self):
        if self.count == 1:
            temp = self.head

            self.head = None
            self.tail = None
            self.count -= 1
            
            return temp

        elif self.count > 1:
            cur = self.head

            while cur.next != self.tail:
                cur = cur.next
            
            temp = self.tail
            cur.next = None
            self.tail = cur

            self.count -= 1
            return temp

        else:
            return None

    def printQueue(self):
        if self.count == 0:
            print("Error : There is no Node")
        else:
            cur = self.head
            print("number of Node : %d"%(self.count))

            while cur:
                print("[%d]"%(cur.data), end=" ")
                cur = cur.next
            print()

    def getSize(self):
        return self.count

if __name__ == '__main__':
    myDeque = Deque()
    n = int(stdin.readline())
    for _ in range(n):
        order = stdin.readline().split()

        if "push_front" in order[0]:
            myDeque.pushfront(int(order[1]))
        elif "push_back" in order[0]:
            myDeque.pushback(int(order[1]))

        elif "pop" in order[0]:
            if "front" in order[0]:
                temp = myDeque.popfront()
            else:
                temp = myDeque.popback()

            if temp != None:
                print(temp)
            else:
                print(-1)

        elif "size" in order[0]:
            print(myDeque.getSize())

        elif "empty" in order[0]:
            if myDeque.getSize() == 0:
                print(1)
            else:
                print(0)

        elif "front" in order[0]:
            if myDeque.head != None:
                print(myDeque.head)
            else:
                print(-1)

        elif "back" in order[0]:
            if myDeque.tail != None:
                print(myDeque.tail)
            else:
                print(-1)
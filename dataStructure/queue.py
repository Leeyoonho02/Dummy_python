from sys import stdin

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def push(self, data):
        newNode = Node(data)

        if self.count == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.count += 1

    def pop(self):
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
            print("Error : There is no Node")

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

if __name__ == '__main__':
    n = int(stdin.readline())
    myQueue = Queue()

    for i in range(1, n+1):
        myQueue.push(i)
    
    myQueue.printQueue()
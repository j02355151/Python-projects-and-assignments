class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CreateList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.current = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        self.size += 1

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            print("Nodes of the circular linked list: ")
            current = self.head
            while True:
                print(current.data, end=" ")
                current = current.next
                if current == self.head:
                    break
            print()

    def search(self, element):
        if self.head is None:
            print(f"{element} not found!")
            return
        temp = self.head
        for _ in range(self.size):
            if temp.data == element:
                print(f"{element} found!")
                return
            temp = temp.next
        print(f"{element} not found!")

    def delete(self):
        if self.head is None:
            return
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        self.size -= 1

    def step(self):
        if self.head is None:
            return
        self.current = self.current.next if self.current else self.head

if __name__ == "__main__":
    cl = CreateList()
    cl.add(2)
    cl.add(2)
    cl.add(3)
    cl.add(4)
    cl.display()
    cl.search(3)
    cl.delete()
    cl.display()
    cl.step()
    cl.display()




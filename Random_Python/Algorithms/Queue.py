# Queue class


class Queue:
    def __init__(self):
        self.items=[]
    def add(self,item):
        self.items.append(item)
    def delete(self):
        itemToRemove = self.items[0]
        del self.items[0]
        return itemToRemove
    def size(self):
        return len(self.items)
    def report(self):
        return self.items
    

def testQueue():
    myQueue=Queue()
    myQueue.add("Bob")
    myQueue.add("Charles")
    myQueue.add("Tim")
    print(myQueue.size())
    print(myQueue.report())
    print(myQueue.delete())
    print(myQueue.report())

class queue:
    def __init__(self):
        self.queue =  list()

    def add(self,value):
        if value not in self.queue:
            self.queue.insert(0,value)
            return True
        return False
    
    def len(self):
        return len(self.queue)

    def showqueue(self):
        if len(self.queue) <= 0:
            return " queue has no element"
        else:
            for i in range(len(self.queue)):
                print(self.queue[i],end=" ")
                
    
    def remove(self):
        if len(self.queue)>0:
            return self.queue.pop()
        else:
            return "queue is empty"

q = queue()
q.add("Mon")
q.add("tue")
q.add("3")

q.remove()
print(q.len())
q.showqueue()

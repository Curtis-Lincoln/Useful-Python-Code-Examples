class Stack(object):
    
    def __init__(self):
        self.content = []

    def Push(self,item):
        self.content.append(item)

    def Peek(self):
        if len(self.content) > 0:
            return self.content[-1]
        else:
            return "EMPTY"

    def Pop(self):
        if len(self.content) > 0:
            top = self.content[-1]
            self.content = self.content[:-1]
            return top
        else:
            return "EMPTY"

class Queue(object):

    def __init__(self):
        self.content = [0] * 5
        self.Limit = 5
        self.Front_Queue = 0
        self.Back_Queue = 0
        self.Full = False

    def Add(self, item):
        if not self.Full:
            self.content[self.Back_Queue] = item
            self.Back_Queue += 1

            if self.Back_Queue >= self.Limit:
                self.Full = True
        return self.content
            

    def Remove(self):
        if self.Front_Queue == self.Back_Queue and not self.Full:
            Element = "EMPTY"
        else:
            Element = self.content[self.Front_Queue]
            self.Front_Queue += 1
            if self.Front_Queue >= self.Limit:
                self.Front_Queue = 0
            self.Full = False
        return self.content
                

    def Peek(self):
        if len(self.content) > 0:
            return self.content[-1]
        else:
            return "EMPTY"



    

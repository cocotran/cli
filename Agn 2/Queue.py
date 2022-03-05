class PriorityQueue():
    def _init_(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) == 0

    #Inserting elemetns based on priority of execution
    def insert(self, data):
        try:
            max = 0 
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max =i 
            item = self.queue[max]
            self.queue.append(data)
            return item
        except  Exception as err:
            print(err)
            exit()
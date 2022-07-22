class MinHeap:
    def __init__(self, capacity):
        self.heap_list = [0] * capacity
        self.capacity = capacity
        self.size = 0
        self.sorted = []
        
    def insert(self, game=["Test Game", 10.99]):
        if(self.full()):
            print("Heap Is Full")
            return False
        self.heap_list[self.size] = game
        self.size += 1
        self.heapify_up()
    
    def heapify_up(self):
        index = self.size - 1
        while (self.has_parent(index) and self.get_parent(index)[1] > self.heap_list[index][1]):
            self.swap(self.parent(index), index)
            index = self.parent(index)
    
    def heapify_down(self):
        index = 0
        while (self.has_left(index)):
            smallerIndex = self.left_child(index)
            if (self.has_right(index) and self.get_right_child(index)[1] < self.get_left_child(index)[1]):
                smallerIndex = self.right_child(index)
            if(self.heap_list[index][1] < self.heap_list[smallerIndex][1]):
                break
            else:
                self.swap(index, smallerIndex)
            index = smallerIndex
    
    def remove_min(self):
        if(self.size == 0):
            print("Empty heap, cannot remove element")
        game = self.heap_list[0]
        self.heap_list[0] = self.heap_list[self.size - 1]
        self.size -= 1
        self.heapify_down()
        return game
    
    def sort(self):
        while self.size > 0:
            self.sorted.append(self.remove_min())

    # Helper Methods
    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def has_parent(self, index):
        return self.parent(index) >= 0

    def has_left(self, index):
        return self.left_child(index) < self.size

    def has_right(self, index):
        return self.right_child(index) < self.size
    
    def full(self):
        return self.size == self.capacity
    
    def swap(self, index_1, index_2):
        temp = self.heap_list[index_1]
        self.heap_list[index_1] = self.heap_list[index_2]
        self.heap_list[index_2] = temp
    
    # Getter methods
    def get_parent(self, index):
        return self.heap_list[self.parent(index)]

    def get_left_child(self, index):
        return self.heap_list[self.left_child(index)]

    def get_right_child(self, index):
        return self.heap_list[self.right_child(index)]

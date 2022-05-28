class ReverseIter:
    def __init__(self, input_list):
        self.list = input_list

    def __iter__(self):
        self.counter = len(self.list) - 1
        return self

    def __next__(self):
        if self.counter >= 0:
            element_of_list = self.list[self.counter]
            self.counter -= 1
            return element_of_list
        else:
            raise StopIteration
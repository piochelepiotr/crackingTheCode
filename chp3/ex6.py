import stack
import ex4

class Cat:
    def __init__(self, name):
        self.name = name

class Dog:
    def __init__(self, name):
        self.name = name

class Shelter:
    def __init__(self):
        self.n = 0
        self.cats = []
        self.dogs = []

    def enqueue(self, x):
        if isinstance(x, Cat):
            self.cats.append((x, self.n))
        elif isinstance(x, Dog):
            self.dogs.append((x, self.n))
        else:
            raise Exception('Unknown animal type')
        self.n += 1

    def dequeue_any(self):
        if len(self.cats) == 0 and len(self.dogs) == 0:
            raise Exception('no more animals')
        if len(self.cats) == 0:
            return self.dequeue_dog()
        if len(self.dogs) == 0:
            return self.dequeue_cat()
        _, n_cat = self.cats[0]
        _, n_dog = self.dogs[0]
        if n_cat < n_dog:
            return self.dequeue_cat()
        return self.dequeue_dog()
    
    def dequeue_dog(self):
        if len(self.dogs) == 0:
            raise Exception('no more dogs')
        x,_ = self.dogs[0]
        del self.dogs[0]
        return x

    def dequeue_cat(self):
        if len(self.cats) == 0:
            raise Exception('no more cats')
        x,_ = self.cats[0]
        del self.cats[0]
        return x



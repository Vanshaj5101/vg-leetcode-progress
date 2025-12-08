class MyHashSet:

    def __init__(self):
        self.n = 1000
        self.arr = [[] for i in range(self.n)]

    def add(self, key: int) -> None:
        index = key % self.n
        if key not in self.arr[index]:
            self.arr[index].append(key)

    def remove(self, key: int) -> None:
        index = key % self.n
        if key in self.arr[index]:
            self.arr[index].remove(key)

    def contains(self, key: int) -> bool:
        index = key % self.n
        print(self.arr[index])
        return key in self.arr[index]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
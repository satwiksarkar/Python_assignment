import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        heapq.heappush(self.heap, (-priority, item))

    def pop(self):
        if not self.heap:
            print("Priority Queue is empty")
            return
        priority, item = heapq.heappop(self.heap)
        print("Removed item:", item)

    def display(self):
        if not self.heap:
            print("Queue is empty")
            return
        print("Current Queue:")
        for p, item in self.heap:
            print(item, "Priority:", -p)


pq = PriorityQueue()

while True:
    print("\n1. Insert Item")
    print("2. Pop Highest Priority Item")
    print("3. Display Queue")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        item = input("Enter item: ")
        priority = int(input("Enter priority: "))
        pq.push(item, priority)

    elif choice == 2:
        pq.pop()

    elif choice == 3:
        pq.display()

    elif choice == 4:
        break

    else:
        print("Invalid choice")
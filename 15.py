# import heapq

# numbers = [12, 3, 45, 7, 23, 9, 30]

# n = int(input("Enter N: "))

# largest = heapq.nlargest(n, numbers)
# smallest = heapq.nsmallest(n, numbers)

# print("Smallest", n, "items:", smallest)
# print("Largest", n, "items:", largest)
import heapq

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
n = int(input("Enter N: "))

print("Largest N items:", heapq.nlargest(n, numbers))
print("Smallest N items:", heapq.nsmallest(n, numbers))
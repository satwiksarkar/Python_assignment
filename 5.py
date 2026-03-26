def fibonacci_generator():
    a, b = 0, 1
    print("\n[Trace] Generator started. Initial state: a=0, b=1")
    
    while True:
        print(f"[Trace] Yielding {a}. Calculating next state...")
        yield a
        c=a+b
        a=b
        b=c
# 2. Memorization Setup
fib_gen = fibonacci_generator()
memoized_fibs = []  # This list will act as our memory/cache

print("--- Getting the First 7 Fibonacci Numbers ---")
for _ in range(7):
    current_number = next(fib_gen)
    memoized_fibs.append(current_number)

print(f"\nMemorized Sequence: {memoized_fibs}")

user_str = input("\nEnter a number to check if its a Fibonacci number: ")

# Make sure they actually entered a number! (Duck typing/validation)
if user_str.isdigit():
    user_num = int(user_str)
    
    while memoized_fibs[-1] < user_num:
        print(f"[Trace] {user_num} is larger than {memoized_fibs[-1]}, generating more...")
        memoized_fibs.append(next(fib_gen))
    if user_num in memoized_fibs:
        print(f"\nYes, {user_num} is a Fibonacci number.")
    else:
        print(f"\nNo, {user_num} is not a Fibonacci number.")
else:
    print("Invalid input. Please enter a positive integer.")
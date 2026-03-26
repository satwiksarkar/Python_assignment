import time
a = int(input("Enter a: "))
q = int(input("Enter q: "))
def geometric_progression(a, q):
    while True:
        yield a
        a *= q
        if a>100000:
            print("Value exceeded 100000, stopping the generator.")
            return
start_total = time.perf_counter() # Start total timer
gp=geometric_progression(a, q)
results=[]
start_loop = time.perf_counter() # Start loop timer

for value in gp:
    results.append(value)

end_loop = time.perf_counter()   # End loop timer
end_total = time.perf_counter()  # End total timer

print("Generated values:", results)
print(f"Time taken for loop execution: {end_loop - start_loop:.6f} seconds")
print(f"Total time taken: {end_total - start_total:.6f} seconds")
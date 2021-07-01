import random
# Random Unique Numbers
def random_sample(count, start, stop, step=1):
    def gen_random():
        while True:
            yield random.randrange(start, stop, step)
# Hash'J Programming
    def gen_n_unique(source, n):
        seen = set()
        seenadd = seen.add
        for i in (i for i in source() if i not in seen and not seenadd(i)):
            yield i
            if len(seen) == n:
                break
    return [i for i in gen_n_unique(gen_random,min(count, int(abs(stop - start) / abs(step))))]
# Hash'J Programming
stored_data = random_sample(999999, 100000, 999999)

# Hash'J Programming
for data in stored_data:
    print(data)
    file = open("PLDT.txt", "a")
    file.write(f"PLDTWIFI{data}\n")
from typing import List
from timeit import timeit
from matplotlib import pyplot as plt
from random import randint


def generate_random_numbers(n: int) -> List[int]:
    numbers = []
    i = 0
    while i != n:
        number = randint(0, 300000)
        if number in numbers:
            continue
        numbers.append(number)
        i += 1
    return numbers


if __name__ == "__main__":
    n_first = [10000, 20000, 50000, 100000]
    times = {
        2: [],
        3: [],
        4: []
    }
    for n in n_first:
        heap_val = generate_random_numbers(n)
        for i in range(2, 5):
            times[i].append(timeit(f"Heap({i}, {heap_val})", setup='from heap import Heap', number=1))
    plt.plot(n_first, times[2], label="Kopiec 2arny")
    plt.plot(n_first, times[3], label="Kopiec 3arny")
    plt.plot(n_first, times[4], label="Kopiec 4arny")
    plt.title('Czas tworzenia kopca')
    plt.legend()
    plt.savefig('create_heap.png')
    plt.clf()
    times = {
        2: [],
        3: [],
        4: []
    }
    for n in n_first:
        heap_val = generate_random_numbers(n)
        for i in range(2, 5):
            times[i].append(timeit(f"for _ in range({n}): heap.extract()", setup=f'from heap import Heap; heap = Heap({i}, {heap_val})', number=1))
    plt.plot(n_first, times[2], label="Kopiec 2arny")
    plt.plot(n_first, times[3], label="Kopiec 3arny")
    plt.plot(n_first, times[4], label="Kopiec 4arny")
    plt.title('Czas usuwania szczytu kopca n razy')
    plt.legend()
    plt.savefig('extract_maximum.png')
    plt.clf()

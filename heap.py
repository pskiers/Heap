from typing import List


class Heap:
    def __init__(self, num_of_sons: int, start_elements: List[int] = None) -> None:
        self._num_of_sons = num_of_sons
        self._elements = []
        if start_elements is not None:
            for element in start_elements:
                self.insert(element)

    def get_nth_son_index(self, n: int, node: int) -> int:
        return self._num_of_sons*node + n

    def get_parent_index(self, node: int) -> int:
        return ((node-1) // self._num_of_sons)

    def extract(self) -> int:
        extracted = self._elements[0]
        self._elements[0] = self._elements[-1]
        self._elements = self._elements[:-1]
        self.heapify_extract(0)
        return extracted

    def heapify_extract(self, start_index) -> None:
        sons_values = dict()
        for n in range(1, self._num_of_sons+1):
            son_index = self.get_nth_son_index(n, start_index)
            if son_index <= len(self._elements) - 1:
                if self._elements[son_index] > self._elements[start_index]:
                    sons_values[self._elements[son_index]] = son_index
        if len(sons_values) != 0:
            daBiggest = max(sons_values.keys())
            self._elements[start_index], self._elements[sons_values[daBiggest]] = self._elements[sons_values[daBiggest]], self._elements[start_index]
            self.heapify_extract(sons_values[daBiggest])

    def heapify_insert(self, start_index) -> None:
        if start_index == 0:
            return
        parent_index = self.get_parent_index(start_index)
        if self._elements[start_index] > self._elements[parent_index]:
            self._elements[start_index], self._elements[parent_index] = self._elements[parent_index], self._elements[start_index]
        return self.heapify_insert(parent_index)

    def insert(self, node: int) -> None:
        self._elements.append(node)
        last_index = len(self._elements) - 1
        self.heapify_insert(last_index)

    def get_rows(self) -> dict:
        values = {}
        next = True
        height = 1
        offset = 0
        while next:
            width = int(self._num_of_sons ** (height - 1))
            for i in range(width):
                if height not in values:
                    values[height] = []
                values[height].append(self._elements[offset])
                if offset + 1 > len(self._elements) - 1:
                    next = False
                    break
                offset += 1
            height += 1
        return values

    def print(self):
        values = self.get_rows()
        max_depth = len(values)

        def max_word_len():
            return max([len(str(i)) for i in self._elements])
        max_word = max_word_len()
        length = (max_word + 1) * self._num_of_sons ** max_depth
        i = 0
        for key in range(1, max_depth+1):
            for numb in values[key]:
                print(str(numb).center(length//self._num_of_sons**i), end="")
            print()
            i += 1

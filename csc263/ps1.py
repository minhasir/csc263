'''
CSC263 Winter 2025
Problem Set 1 Starter Code
University of Toronto Mississauga
'''


# Do NOT add any "import" statements
# i hate heaps. the dirty bubble q.q

def spy263(commands):
    '''
    Pre: commands is a list of commands
    Post: return list of find_spy results
    '''

    # Max Heap
    def insert_max(heap, x):
        '''
        Helper function that inserts into the heap use bubble_up_max when inserting and extract_max/bubble_down when
        the kth smallest element is no longer the root.
        '''
        heap.append(x)
        bubble_up_max(heap, len(heap) - 1)

    def bubble_up_max(heap, index):
        parent = (index - 1) // 2  # i-1/2 rounded down cuz start at 0
        while index > 0 and heap[index] > heap[parent]:
            heap[index], heap[parent] = heap[parent], heap[index]  # parallel assignment
            index = parent
            parent = (index - 1) // 2

    def bubble_down(heap, index):
        n = len(heap)

        left_child = 2 * index + 1
        right_child = 2 * index + 2
        parent = index

        if left_child < n and heap[left_child] > heap[parent]:
            parent = left_child
        if right_child < n and heap[right_child] > heap[parent]:
            parent = right_child
        if parent != index:
            heap[index], heap[parent] = heap[parent], heap[index]
            bubble_down(heap, parent)

    def extract_max(heap):
        if not heap:
            return None
        max_val = heap[0]
        heap[0] = heap.pop()
        bubble_down(heap, 0)
        return max_val

    # Min Heap
    def insert_min(heap, x):
        heap.append(x)
        bubble_up_min(heap, len(heap) - 1)

    def bubble_up_min(heap, index):
        parent = (index - 1) // 2
        while index > 0 and heap[index] < heap[parent]:
            heap[index], heap[parent] = heap[parent], heap[index]
            index = parent
            parent = (index - 1) // 2

    def bubble_down_min(heap, index):
        n = len(heap)
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        parent = index

        if left_child < n and heap[left_child] < heap[parent]:
            parent = left_child
        if right_child < n and heap[right_child] < heap[parent]:
            parent = right_child
        if parent != index:
            heap[index], heap[parent] = heap[parent], heap[index]
            bubble_down_min(heap, parent)

    def extract_min(heap):
        if not heap:
            return None
        min_val = heap[0]
        heap[0] = heap.pop()
        bubble_down_min(heap, 0)
        return min_val
# Actual Code
    n = 0
    max_heap = []
    min_heap = []

    theta = 0.263
    collection = []
    for command in commands:
        if command == 'find_spy':
            collection.append(max_heap[0])
        else:
            x = int(command.split()[1])
            n += 1
            k = -int(-1 * (theta * n) // 1)

            if len(max_heap) == 0 or x <= max_heap[0]:
                insert_max(max_heap, x)
            else: # may be sus.
                insert_min(min_heap, x)
            if len(max_heap) > k:
                insert_min(min_heap, extract_max(max_heap))
            if len(max_heap) < k:
                insert_max(max_heap, extract_min(min_heap))

    return collection


# You may add additional test case below. HOWEVER, your code must
# compile and be runnable in order to earn any credit for correctness.

if __name__ == '__main__':
    # some small test cases (1, 1, 1, 2, 2, 2, 2, 3)
    assert [15, 6, 2] == spy263(
        ['insert 15',
         'find_spy',
         'insert 6',
         'insert 2',
         'insert 8',
         'find_spy',
         'insert -5',
         'insert -8',
         'insert 3',
         'insert 20',
         'find_spy',
         ])
    assert [2, 3, 2, 3] == spy263(
        ['insert 7',
         'insert 2',
         'find_spy',
         'insert 3',
         'insert 8',
         'find_spy',
         'insert 6',
         'insert 5',
         'insert 1',
         'find_spy',
         'insert 4',
         'find_spy',
         ])
    assert [1, 1] == spy263(
        ['insert 1',
         'insert 2',
         'insert 3',
         'find_spy',
         'find_spy'])
    assert [1, 1, 1] == spy263(
        ['insert 1',
         'insert 2',
         'insert 1',
         'find_spy',
         'find_spy',
         'insert 1',
         'find_spy'])

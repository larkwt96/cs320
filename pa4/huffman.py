import sys
import math

db = False
swap_count = 0
heapify_call_count = 0


def reset_counts():
    global swap_count
    swap_count = 0
    global heapify_call_count
    heapify_call_count = 0

    
def swap(A, i, j):
    global swap_count
    swap_count += 1
    A[i], A[j] = A[j], A[i]

    
def count_heapify():
    global heapify_call_count
    heapify_call_count += 1

    
def current_counts():
    return {'swap_count': swap_count, 'heapify_call_count': heapify_call_count}


def readNums(filename):
    """
    Reads a text file containing whitespace separated numbers. Returns a list
    of those numbers.
    """
    with open(filename) as f:
        lst = [int(x) for line in f for x in line.strip().split() if x]
        if db:
            print("List read from file {}: {}".format(filename, lst))
        return lst

    
# heaps here are complete binary trees allocated in arrays (0 based)
def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return left(i) + 1

# END DO NOT MODIFY

def heapify(A, i, n=None):
    """
    Ensure that the tree rooted at element i in the list A is a heap, assuming
    that the trees rooted at elements left(i) and right(i) are already heaps.
    Obviously, if left(i) or right(i) are >= len(A), then element i simply does
    not have those out-of-bounds children. In order to implement an in-place
    heap sort, we will sometimes need to consider the tail part of A as
    out-of-bounds, even though elements do exist there. So instead of comparing
    with len(A), use the parameter n to determine if the child "exists" or not.
    If n is not provided, it defaults to None, which we check for and then set
    n to len(A).

    Since the (up to) two child trees are already heaps, we just need to find
    the right place for the element at i. If it is smaller than both its
    children, then nothing more needs to be done, it's already a min heap.
    Otherwise you should swap the root with the smallest child and recursively
    heapify that tree.

    ***NEW***

    If you determine that the element at i should swap with one of its children
    nodes, MAKE SURE you do this by calling the swap function defined above.
    """
    count_heapify() # This should be the first line of the heapify function, don't change.
    if n is None:
        n = len(A)
    if not(i < n):
        # if asked to heapify an element not below n (the conceptual size of the heap), just return
        # because no work is required
        return
    v = A[i] # parent value
    ri = right(i) # right index
    li = left(i) # left index
    # note: li >= n => ri >= n since ri > li
    if li >= n: # no children exist, no work
        return
    elif ri >= n: # left child exists
        si = li
        sv = A[li]
    else: # both children exist
        # comparison
        if A[ri] < A[li]: # right child smaller
            si = ri
            sv = A[ri]
        else: # left child bigger (or equal)
            si = li
            sv = A[li]

    # si contains potential swap child index
    # sv contains potential swap child value
    # comparison
    if sv < v: # one child bigger
        swap(A, i, si)
        heapify(A, si, n)


def buildHeap(A):
    """
    Turn the list A (whose elements could be in any order) into a heap. Call
    heapify on all the internal nodes, starting with the last internal node,
    and working backwards to the root.
    """
    n = len(A)
    # first parent with children is parent of last element
    i = parent(n-1)
    while i >= 0:
        heapify(A, i, n)
        i -= 1

def heapExtractMin(A):
    """
    Extract the min element from the heap A. Make sure that A is a valid heap
    afterwards. Return the extracted element. This operation should perform
    approximately log_2(len(A)) comparisons and swaps (heapify calls and swap
    calls). Your implementation should not perform O(n) (linear) work.
    """
    if len(A) == 1:
        return A.pop()
    ret = A[0]
    A[0] = A.pop()
    heapify(A, 0)
    return ret

def heapInsert(A, v):
    """
    Insert the element v into the heap A. Make sure that A is a valid heap
    afterwards. This operation should perform approximately log_2(len(A))
    comparisons and swaps (swap calls). Your implementation should not perform
    O(n) (linear) work. MAKE SURE you swap elements by calling the swap
    function defined above.
    """
    i = parent(len(A))
    A.append(v)
    while i > 0:
        heapify(A, i)
        i = parent(i)
    heapify(A, i)

def heapSort(A):
    """
    Sort the list A (in place) using the heap sort algorithm, into descending
    order. Start by using buildHeap. For example, if A = [4, 2, 1, 3, 5].
    After calling heapSort(A), then A should be [5, 4, 3, 2, 1].
    """
    if db:
        print('before heap')
        print(A)
    buildHeap(A)
    n = len(A)
    while n - 1 > 0:
        if db:
            print('sorting with n = ' + str(n))
            print(A)
        tmp = A[0]
        A[0] = A[n-1]
        A[n-1] = tmp
        n -= 1
        heapify(A, 0, n)
        if db:
            print('post: ')
            print(A)

def printHeap(A):
    height = int(math.log(len(A), 2))
    width = len(str(max(A)))
    for i in range(height + 1):
        print(width * (2 ** (height - i) - 1) * " ", end="")
        for j in range(2 ** i):
            idx = 2 ** i - 1 + j
            if idx >= len(A):
                print()
                break
            if j == 2 ** i - 1:
                print("{:^{width}}".format(A[idx], width=width))
            else:
                print("{:^{width}}".format(A[idx], width=width),
                      width * (2 ** (height - i + 1) - 1) * " ", sep='', end='')
    print()


def shuffled_list(length, seed):
    A = list(range(10, length + 10))
    import random
    r = random.Random(seed) # pseudo random, so it is repeatable
    r.shuffle(A)
    return A


def report_counts_on_basic_ops(A, loop_extracts=1, loop_inserts=1):
    original_len = len(A)
    print("\nREPORT on list of len: {}".format(original_len))
    reset_counts()
    buildHeap(A)
    print("buildHeap(A):           \t", current_counts())

    reset_counts()
    m = heapExtractMin(A)
    print("heapExtractMin(A) => {}:\t".format(m), current_counts())

    reset_counts()
    heapInsert(A, m)
    print("heapInsert(A, {}):       \t".format(m), current_counts())

    for i in range(loop_extracts):
        reset_counts()
        m = heapExtractMin(A)
        print("heapExtractMin(A) => {}:\t".format(m), current_counts())

    import random
    r = random.Random(0)
    for i in range(loop_inserts):
        reset_counts()
        new_number = r.randrange(0, original_len // 8)
        heapInsert(A, new_number)
        print("heapInsert(A, {}):       \t".format(new_number), current_counts())

def file_character_frequencies(file_name):
    """Return frequency of characters in file_name."""
    freq = {}
    contents = ""
    with open(file_name) as f:
        contents = f.read()
    for c in contents:
        if not c in freq:
            freq[c] = 0
        freq[c] += 1
    return freq

class PriorityTuple(tuple):
    """A specialization of tuple that compares only its first item when sorting.
    Create one like this: PriorityTuple((x, y, z)) # note the doubled parens"""
    def __lt__(self, other):
        return self[0] < other[0]

    def __le__(self, other):
        return self[0] <= other[0]

def decode_huffman_graph(graph, huffmanCodes, prefix = ''):
    if len(graph) == 2:
        huffmanCodes[graph[1]] = prefix 
    else:
        decode_huffman_graph(graph[1], huffmanCodes, prefix+'0')
        decode_huffman_graph(graph[2], huffmanCodes, prefix+'1')

def huffman_codes_from_frequencies(frequencies):
    """Return dictionary of characters to huffman codes."""
    freqMinHeap = [PriorityTuple((frequencies[c], c)) for c in frequencies]
    buildHeap(freqMinHeap)
    
    while len(freqMinHeap) > 1:
        lmin = heapExtractMin(freqMinHeap)
        rmin = heapExtractMin(freqMinHeap)
        node = PriorityTuple((lmin[0]+rmin[0], lmin, rmin))
        heapInsert(freqMinHeap, node)

    huffmanCodes = {}
    decode_huffman_graph(freqMinHeap[0], huffmanCodes)
    print(freqMinHeap[0])
    return huffmanCodes
    

def huffman_letter_codes_from_file_contents(file_name):
    """WE WILL GRADE BASED ON THIS FUNCTION."""
    freqs = file_character_frequencies(file_name)
    return huffman_codes_from_frequencies(freqs)

def encode_file_using_codes(file_name, letter_codes):
    """Provided to help you play with your code."""
    contents = ""
    with open(file_name) as f:
        contents = f.read()
    file_name_encoded = file_name + "_encoded"
    with open(file_name_encoded, 'w') as fout:
        for c in contents:
            fout.write(letter_codes[c])
    print("Wrote encoded text to {}".format(file_name_encoded))


def decode_file_using_codes(file_name_encoded, letter_codes):
    """Provided to help you play with your code."""
    contents = ""
    with open(file_name_encoded) as f:
        contents = f.read()
    file_name_encoded_decoded = file_name_encoded + "_decoded"
    codes_to_letters = {v: k for k, v in letter_codes.items()}
    with open(file_name_encoded_decoded, 'w') as fout:
        num_decoded_chars = 0
        partial_code = ""
        while num_decoded_chars < len(contents):
            partial_code += contents[num_decoded_chars]
            num_decoded_chars += 1
            letter = codes_to_letters.get(partial_code)
            if letter:
                fout.write(letter)
                partial_code = ""
    print("Wrote decoded text to {}".format(file_name_encoded_decoded))


def main():
    """Provided to help you play with your code."""
    import pprint
    file_name = sys.argv[1]
    frequencies = file_character_frequencies(file_name)
    pprint.pprint(frequencies)
    codes = huffman_codes_from_frequencies(frequencies)
    pprint.pprint(codes)
    encode_file_using_codes(file_name, codes)
    decode_file_using_codes(file_name+'_encoded', codes)


if __name__ == '__main__':
    """We are NOT grading you based on main, this is for you to play with."""
    main()

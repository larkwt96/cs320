import sys
import math

db = False

# provided
def readNums(filename):
    """
    Reads a text file containing whitespace separated numbers.  Returns a list
    of those numbers
    """
    with open(filename) as f:
        lst = [int(x) for line in f for x in line.strip().split() if x]
        if db:
            print("List read from file {}: {}".format(filename, lst))
        return lst

# provided
# heaps here are complete binary trees allocated in arrays (0 based)
def parent(i):
    return (i - 1) // 2

def left(i):
    return 2 * i + 1

def right(i):
    return left(i) + 1

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
    """
    if n is None:
        n = len(A)
    if not(i < n):
        # if asked to heapify an element not below n (the conceptual size of
        # the heap), just return because no work is required
        return
    pass #TODO

def buildHeap(A):
    """
    Turn the list A (whose elements could be in any order) into a
    heap. Use heapify.
    """
    pass #TODO

def heapExtractMin(A):
    """
    Extract the min element from the heap A. Make sure that A is a valid heap
    afterwards. Return the extracted element.
    """
    pass #TODO

def heapInsert(A, v):
    """
    Insert the element v into the heap A. Make sure that A is a valid heap
    afterwards.
    """
    pass #TODO

def heapSort(A):
    """
    Sort the list A (in place) using the heap sort algorithm, into descending
    order.  Start by using buildHeap.
    For example, if A = [4, 2, 1, 3, 5]. After calling heapSort(A), then A
    should be [5, 4, 3, 2, 1].
    """
    pass #TODO

# provided
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
                      width * (2 ** (height - i + 1) - 1) * " ",
                      sep='',
                      end="")
    print()

# provided
def main():
    testA = []
    heapInsert(testA, 5)
    heapInsert(testA, 7)
    heapInsert(testA, 3)
    heapInsert(testA, 1)
    printHeap(testA)
    m = heapExtractMin(testA)
    print("min:", m, "testA:", testA)
    m = heapExtractMin(testA)
    print("min:", m, "testA:", testA)
    m = heapExtractMin(testA)
    print("min:", m, "testA:", testA)
    m = heapExtractMin(testA)
    print("min:", m, "testA:", testA)

    global db
    if len(sys.argv) > 2:
        db = True
    A = readNums(sys.argv[1])
    if db: print("Input:", A)
    buildHeap(A)
    if db: print("heap:", A)
    x = heapExtractMin(A)
    print("min", x)
    if db: print("heap:", A)
    heapInsert(A, 0)
    if db: print("heap:", A)
    x = heapExtractMin(A)
    print("min", x)
    if db: print("heap:", A)
    x = heapExtractMin(A)
    print("min", x)
    if db: print("heap:", A)
    heapSort(A)
    print("reverse sorted A:", A)


if __name__ == "__main__":
    main()

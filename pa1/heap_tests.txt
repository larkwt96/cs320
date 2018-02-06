from argparse import ArgumentParser
import heap


def test_heapify():
    print("#test_heapify")
    A = [1]
    heap.heapify(A, 0)
    print("Heapify length 1:", A == [1])

    A = [2, 1]
    heap.heapify(A, 0)
    print("Heapify two out of order:", A == [1, 2])

    A = [1, 2]
    heap.heapify(A, 0)
    print("Heapify two in order:", A == [1, 2])

    A = [1, 4, 3, 5, 2]
    heap.heapify(A, 1)
    print("Heapify five needing swap:", A == [1, 2, 3, 5, 4])

    A = [1, 8, 3, 9, 2, 10, 11, 12, 13, 7, 6]
    heap.heapify(A, 1)
    print("Heapify five needing recursive swap:", A == [1, 2, 3, 9, 6, 10, 11, 12, 13, 7, 8])

    A = [1, 4, 3, 5, 2]
    heap.heapify(A, 1, 4)
    print("Heapify five with limit number:", A == [1, 4, 3, 5, 2])


def is_min_heap(A):
    def parent(i):
        return (i - 1) // 2
    return all(A[parent(x)] <= A[x] for x in range(1, len(A)))


def shuffled_list(length, seed):
    A = list(range(10, length + 10))
    import random
    r = random.Random(seed) # pseudo random, so it is repeatable
    r.shuffle(A)
    return A


def test_build_heap():
    print("#test_build_heap")
    for x in range(5, 41, 5):
        A = shuffled_list(x, x)
        heap.buildHeap(A)
        print("buildHeap(shuffled_list({}, {})) is a min heap: ".format(x, x), is_min_heap(A))


def test_insert_extract():
    print("#test_insert_extract")
    for round in range(3):
        order = shuffled_list(50, round)
        A = []
        for x in range(20):
            heap.heapInsert(A, order.pop())
            heap.heapInsert(A, order.pop())
            has_heap_property = is_min_heap(A)
            min_elem = min(A)
            extracted = heap.heapExtractMin(A)
            print("Correctly extracted min: {}, maintained heap property: {}".format(
                min_elem == extracted, has_heap_property and is_min_heap(A)))


def test_all():
    test_heapify()
    test_build_heap()
    test_insert_extract()


def test_by_number(test_number):
    if test_number == 1:
        test_heapify()
    elif test_number == 2:
        test_build_heap()
    else:
        test_insert_extract()


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--test", dest="test_number",
                        type=int, help="The number of the test to run [1-3]")
    args = parser.parse_args()
    if args.test_number:
        test_by_number(args.test_number)
    else:
        test_all()

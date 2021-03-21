import logging

from algorithms.BSearch import binary_search
from algorithms.BSearchAns import binary_search_by_answer
from algorithms.addition import addition

ADDING_IN = [f"tests\\addition\\{i}.in" for i in range(1, 3)]
ADDING_OUT = [f"tests\\addition\\{i}.out" for i in range(1, 3)]

BINARY_SEARCH_IN = [f"tests\\binary-search\\{i}.in" for i in range(1, 6)]
BINARY_SEARCH_OUT = [f"tests\\binary-search\\{i}.out" for i in range(1, 6)]

BINARY_SEARCH_BY_RESULTS_IN = [f"tests\\binary-search-by-results\\{i}.in" for i in range(1, 6)]
BINARY_SEARCH_BY_RESULTS_OUT = [f"tests\\binary-search-by-results\\{i}.out" for i in range(1, 6)]

BINARY_TREE_IN = [f"tests\\binary-tree\\{i}.in" for i in range(1, 8)]
BINARY_TREE_CONTAINS_OUT = [f"tests\\binary-tree\\{i}.contains.out" for i in range(1, 8)]
BINARY_TREE_MIN_AFTER_OUT = [f"tests\\binary-tree\\{i}.min-after.out" for i in range(1, 8)]

logging.basicConfig(level=logging.INFO)


def adding_test():
    log = logging.getLogger("Adding")
    for file_id in range(len(ADDING_IN)):
        log.info(f"Test {file_id + 1}...")
        fin = open(ADDING_IN[file_id], "r")
        fout = open(ADDING_OUT[file_id], "r")
        a = int(fin.readline())
        flag = True
        for i in range(a):
            x, y = fin.readline().replace('\n', '').split(' ')
            get_result: str = addition(x, y)
            right_answer: str = fout.readline().replace('\n', '')
            if get_result != right_answer:
                log.info(
                    f"Test {file_id + 1} failed on the position {i} ({x, y}): expected {right_answer},"
                    f"were got {get_result}")
                flag = False

            if not flag:
                break

        if flag:
            log.info(f"Test {file_id + 1} passed!")
        fin.close()
        fout.close()


def binary_search_test():
    log = logging.getLogger("BinarySearch")
    for file_id in range(len(BINARY_SEARCH_IN)):
        log.info(f"Test {file_id + 1}...")
        fin = open(BINARY_SEARCH_IN[file_id], "r")
        fout = open(BINARY_SEARCH_OUT[file_id], "r")
        n = int(fin.readline())
        array = fin.readline().split()
        array = [int(i) for i in array]
        k = int(fin.readline())
        flag = True
        for i in range(k):
            val = int(fin.readline())
            right_answer: int = int(fout.readline())
            get_result: int = binary_search(array, val, right=n - 1)
            if get_result != right_answer:
                log.info(
                    f"Test {file_id + 1} failed on the position {i} ({val}): expected {right_answer},"
                    f" were got {get_result}")
                flag = False
            if not flag:
                break
        if flag:
            log.info(f"Test {file_id + 1} passed!")
        fin.close()
        fout.close()


def binary_search_by_answer_test():
    log = logging.getLogger("BinarySearchOnTheResult")
    for file_id in range(len(BINARY_SEARCH_BY_RESULTS_IN)):
        log.info(f"Test {file_id + 1}...")
        fin = open(BINARY_SEARCH_BY_RESULTS_IN[file_id], "r")
        fout = open(BINARY_SEARCH_BY_RESULTS_OUT[file_id], "r")
        N = int(fin.readline())
        k = int(fin.readline())
        array = []
        for i in range(N):
            array.append(int(fin.readline()))
        get_result: int = binary_search_by_answer(array, N, k, right=array[-1])
        right_answer: int = int(fout.readline())

        if (get_result != right_answer):
            log.info(
                f"Test {file_id + 1} failed: expected {right_answer}, were got {get_result}")
        else:
            log.info(f"Test {file_id + 1} passed!")

        fin.close()
        fout.close()


def default_binary_tree_test():
    log = logging.getLogger("BinaryTree")
    for file_id in range(len(BINARY_TREE_IN)):
        log.info(f"Test {file_id + 1}...")
        fin = open(BINARY_TREE_IN[file_id], "r")
        fout = open(BINARY_TREE_CONTAINS_OUT[file_id], "r")
        fout2 = open(BINARY_TREE_MIN_AFTER_OUT[file_id], "r")
        N = int(fin.readline())
        k = int(fin.readline())
        array = []
        for i in range(N):
            array.append(int(fin.readline()))
        get_result: int = binary_search_by_answer(array, N, k, right=array[-1])
        right_answer: int = int(fout.readline())

        if (get_result != right_answer):
            log.info(
                f"Test {file_id + 1} failed: expected {right_answer}, were got {get_result}")
        else:
            log.info(f"Test {file_id + 1} passed!")

        fin.close()
        fout.close()


if __name__ == '__main__':
    adding_test()
    # binary_search_test()
    binary_search_by_answer_test()

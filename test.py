import logging
import os
from logging import Logger
from typing import TextIO

from algorithms.BSearch import binary_search
from algorithms.BSearchAns import binary_search_by_answer
from algorithms.DisjointSetUnion import Node, unite, text_test
from algorithms.addition import addition

ADDING_TESTS = 'tests\\addition'

BINARY_SEARCH_TESTS = 'tests\\binary-search'

BINARY_SEARCH_BY_RESULTS_TESTS = 'tests\\binary-search-by-results'

BINARY_TREE_IN = [f"tests\\binary-tree\\{i}.in" for i in range(1, 8)]
BINARY_TREE_CONTAINS_OUT = [f"tests\\binary-tree\\{i}.contains.out" for i in range(1, 8)]
BINARY_TREE_MIN_AFTER_OUT = [f"tests\\binary-tree\\{i}.min-after.out" for i in range(1, 8)]

UFF_TEST = 'tests\\uff'

logging.basicConfig(level=logging.INFO)


def generator_test_files(directory: str, log: Logger):
    """ Генератор входных и проверочных файлов для тестов.

    :type log: Logger
    :type directory: str
    """
    for file in os.listdir(directory):
        if file.endswith('.in'):
            file = file[0:-3]
            log.info(f"Test {file}...")
            fin: TextIO = open(directory + '\\' + file + '.in', "r")
            fout: TextIO = open(directory + '\\' + file + '.out', "r")
            yield fin, fout, file


def adding_test():
    log: Logger = logging.getLogger("Adding")
    for fin, fout, file in generator_test_files(ADDING_TESTS, log):
        a = int(fin.readline())
        flag = True
        for i in range(a):
            x, y = fin.readline().replace('\n', '').split(' ')
            get_result: str = addition(x, y)
            right_answer: str = fout.readline().replace('\n', '')
            if get_result != right_answer:
                log.info(
                    f"Test {file} failed on the position {i} ({x, y}): expected {right_answer},"
                    f"were got {get_result}")
                flag = False

            if not flag:
                break

        if flag:
            log.info(f"Test {file} passed!")
        fin.close()
        fout.close()


def binary_search_test():
    log = logging.getLogger("BinarySearch")
    for fin, fout, file in generator_test_files(BINARY_SEARCH_TESTS, log):
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
                    f"Test {file} failed on the position {i} ({val}): expected {right_answer},"
                    f" were got {get_result}")
                flag = False
            if not flag:
                break
        if flag:
            log.info(f"Test {file} passed!")
        fin.close()
        fout.close()


def binary_search_by_answer_test():
    log = logging.getLogger("BinarySearchByAnswer")
    for fin, fout, file in generator_test_files(BINARY_SEARCH_BY_RESULTS_TESTS, log):

        N = int(fin.readline())
        k = int(fin.readline())
        array = []
        for i in range(N):
            array.append(int(fin.readline()))
        get_result: int = binary_search_by_answer(array, N, k, right=array[-1])
        right_answer: int = int(fout.readline())

        if (get_result != right_answer):
            log.info(
                f"Test {file} failed: expected {right_answer}, were got {get_result}")
        else:
            log.info(f"Test {file} passed!")

        fin.close()
        fout.close()


def CHM_test():
    log = logging.getLogger("CHM")
    for fin, fout, file in generator_test_files(UFF_TEST, log):
            n: list = fin.readline().split()
            dict = {}
            for i in range(int(n[-1])):
                array = fin.readline().split()
                for num in array:
                    if dict.get(num) is None:
                        dict[num] = Node(num)
                get_result = text_test(dict[array[0]], dict[array[1]])
                if get_result == 'NO':
                    unite(dict[array[0]], dict[array[1]])
                right_answer = fout.readline().replace('\n', '')
                if not get_result == right_answer:
                    log.info(
                        f"Test {file} failed: expected {right_answer}, were got {get_result}")
            log.info(f"Test {file} passed!")


def default_binary_tree_test():
    """ Не рабочий кусок кода не тройгайте пожалуйста, возможно его починят"""
    # TODO Сделать тестирование бинарного дерева
    log = logging.getLogger("BinaryTree")
    for file in range(len(BINARY_TREE_IN)):
        log.info(f"Test {file + 1}...")
        fin = open(BINARY_TREE_IN[file], "r")
        fout = open(BINARY_TREE_CONTAINS_OUT[file], "r")
        fout2 = open(BINARY_TREE_MIN_AFTER_OUT[file], "r")
        N = int(fin.readline())
        k = int(fin.readline())
        array = []
        for i in range(N):
            array.append(int(fin.readline()))
        get_result: int = binary_search_by_answer(array, N, k, right=array[-1])
        right_answer: int = int(fout.readline())

        if (get_result != right_answer):
            log.info(
                f"Test {file + 1} failed: expected {right_answer}, were got {get_result}")
        else:
            log.info(f"Test {file + 1} passed!")

        fin.close()
        fout.close()



if __name__ == '__main__':
    adding_test()
    binary_search_test()
    binary_search_by_answer_test()
    CHM_test()

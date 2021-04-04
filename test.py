import logging
import os
from logging import Logger
from typing import TextIO

from tqdm import tqdm

from algorithms.BSearch import binary_search
from algorithms.BSearchAns import binary_search_by_answer
from algorithms.BinaryTree import BinaryTree, Treap
from algorithms.DisjointSetUnion import Node, unite, text_test
from algorithms.addition import addition

ADDING_TESTS = 'tests\\addition'
BINARY_SEARCH_TESTS = 'tests\\binary-search'
BINARY_SEARCH_BY_RESULTS_TESTS = 'tests\\binary-search-by-results'
UFF_TESTS = 'tests\\uff'
BLOCKS_ON_THE_PICTURE_TESTS = 'tests\\blocks'
BINARY_TREE = 'tests\\binary-tree'

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


def generator_test_files_for_binary_tree(directory: str, log: Logger):
    """ Генератор входных и проверочных файлов для тестов деревьев.

    :type log: Logger
    :type directory: str
    """
    for file in os.listdir(directory):
        if file.endswith('.in'):
            file = file[0:-3]
            log.info(f"Test {file}...")
            fin: TextIO = open(directory + '\\' + file + '.in', "r")
            fout: TextIO = open(directory + '\\' + file + '.contains.out', "r")
            fout2: TextIO = open(directory + '\\' + file + '.min-after.out', "r")

            yield fin, fout, fout2, file


def log_result_test(get_result, right_answer, test_name: str, log: Logger) -> bool:
    """
    Логирует ошибки если они есть, а также возвращет результат прохождения теста.

    :rtype bool
    """
    if not get_result == right_answer:
        log.info(
            f"Test {test_name} failed: expected {right_answer}, were got {get_result}")
    return get_result == right_answer


def adding_test():
    log: Logger = logging.getLogger("Adding")
    for fin, fout, file in generator_test_files(ADDING_TESTS, log):
        a = int(fin.readline())
        flag = True
        for i in tqdm(range(a)):
            x, y = fin.readline().replace('\n', '').split(' ')
            get_result: str = addition(x, y)
            right_answer: str = fout.readline().replace('\n', '')
            log.debug(f"File {file}: the program received {get_result}, when {right_answer} was expected.")
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
        for i in tqdm(range(k)):
            val = int(fin.readline())
            right_answer: int = int(fout.readline())
            get_result: int = binary_search(array, val, right=n - 1)
            log.debug(f"File {file}: the program received {get_result}, when {right_answer} was expected.")
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
        log.debug(f"File {file}: the program received {get_result}, when {right_answer} was expected.")
        if (get_result != right_answer):
            log.info(
                f"Test {file} failed: expected {right_answer}, were got {get_result}")
        else:
            log.info(f"Test {file} passed!")

        fin.close()
        fout.close()


def CHM_test():
    log = logging.getLogger("CHM")
    for fin, fout, file in generator_test_files(UFF_TESTS, log):
        n: list = fin.readline().split()
        dict = {}
        flag = True
        for i in tqdm(range(int(n[-1]))):
            array = fin.readline().split()
            for num in array:
                if dict.get(num) is None:
                    dict[num] = Node(num)
            get_result = text_test(dict[array[0]], dict[array[1]])
            if get_result == 'NO':
                unite(dict[array[0]], dict[array[1]])
            right_answer = fout.readline().replace('\n', '')
            log.debug(f"File {file}: the program received {get_result}, when {right_answer} was expected.")
            if not get_result == right_answer:
                log.info(
                    f"Test {file} failed: expected {right_answer}, were got {get_result}")
                flag = False
        if flag:
            log.info(f"Test {file} passed!")

        fin.close()
        fout.close()


def blocks_on_the_picture():
    log = logging.getLogger('Picture')
    for fin, fout, file in generator_test_files(BLOCKS_ON_THE_PICTURE_TESTS, log):
        n = fin.readline().split()
        prev = fin.readline().replace('\n', '')
        array = {}
        left = False
        for j in range(len(prev)):
            if prev[j] == '1':
                array[(0, j)] = Node((0, j))
                if left:
                    unite(array[(0, j)], array[(0, j - 1)])
                left = True
            else:
                left = False
        left = False
        for i in tqdm(range(1, int(n[0]))):
            current = fin.readline().replace('\n', '')
            for j in range(len(current)):
                if current[j] == '1':
                    array[(i, j)] = Node((i, j))
                    if left:
                        unite(array[(i, j)], array[(i, j - 1)])
                    if prev[j] == '1':
                        unite(array[(i - 1, j)], array[(i, j)])
                    left = True
                else:
                    left = False
            prev = current
            left = False
        hash_table = set()
        for i in array.values():
            hash_table.add(i.find())
        get_result = len(hash_table)
        right_answer = int(fout.readline().replace('\n', ''))
        log.debug(f"File {file}: the program received {get_result}, when {right_answer} was expected.")
        if not get_result == right_answer:
            log.info(
                f"Test {file} failed: expected {right_answer}, were got {get_result}")
        else:
            log.info(f"Test {file} passed!")

        fin.close()
        fout.close()


def _binary_tree_test_utils(fout, fout2, get_result_contains, get_result_min_after, file, log: Logger) -> bool:
    right_answer_contains: str = fout.readline().replace('\n', '')
    right_answer_min_after: str = fout2.readline().replace('\n', '')
    flag = log_result_test(get_result_contains, right_answer_contains,
                           '{}.{}'.format(file, 'contains'), log)
    flag = flag if log_result_test(get_result_min_after, right_answer_min_after,
                                   '{}.{}'.format(file, 'min-after'), log) else False
    return flag


def binary_tree_test(Tree):
    """ Тестирует деревья, наследующие интерфейс BinaryTree, принимает в себя тестируемый класс"""
    log = logging.getLogger(Tree.__name__)
    for fin, fout, fout2, file in generator_test_files_for_binary_tree(BINARY_TREE, log):
        n = int(fin.readline())
        current_value = int(fin.readline())
        tree = Tree(current_value)
        get_result_contains = '-'
        get_result_min_after = '- -'
        _binary_tree_test_utils(fout, fout2, get_result_contains, get_result_min_after, file, log)
        flag = True
        for i in tqdm(range(n - 1)):
            current_value = int(fin.readline())
            try:
                get_result_contains: str = tree.text_find_node(current_value)
                if get_result_contains == '-':
                    tree.add_node(current_value)
                get_result_min_after = '{} {}'.format(get_result_contains,
                                                      tree.text_find_next_node(current_value))
            except RecursionError:
                flag = False
                log.info(f"Test {file} failed: the tree has too much depth")
                break
            flag = flag if _binary_tree_test_utils(fout,
                                                   fout2,
                                                   get_result_contains,
                                                   get_result_min_after,
                                                   file,
                                                   log) else False
        else:
            if flag:
                log.info(f"Test {file} passed!")

        fin.close()
        fout.close()


if __name__ == '__main__':
    adding_test()
    binary_search_test()
    binary_search_by_answer_test()
    CHM_test()
    blocks_on_the_picture()
    binary_tree_test(BinaryTree)
    binary_tree_test(Treap)

import logging

from algorithms.addition import addition

ADDING_IN = [f"tests\\addition\\{i}.in" for i in range(1, 3)]
ADDING_OUT = [f"tests\\addition\\{i}.out" for i in range(1, 3)]

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


if __name__ == '__main__':
    adding_test()

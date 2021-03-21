import itertools


def addition(a: object, b: object) -> str:
    """

    Сложение двух длиных чисел, числа могут быть представлены как целые,
    так и как строки.
    :rtype: str
    """
    if isinstance(a, int) and isinstance(b, int):
        return str(a + b)
    else:
        a, b = str(a)[::-1], str(b)[::-1]
        mod = 0
        result = []
        for i, j in itertools.zip_longest(a, b):
            if i is None:
                i = 0
            if j is None:
                j = 0
            result.append(str((int(i) + int(j) + mod) % 10))
            mod = (int(i) + int(j) + mod) // 10
        if mod > 0:
            result.append(str(mod))
        result.reverse()
        return ''.join(result)


if __name__ == "__main__":
    print(addition("1345674", "1345432"))
    print(addition(1344, 1324))
    print(addition("98765433456786543234567654324567865434567876543",
                   "2345676543234567654323456765432456765432345676543"))

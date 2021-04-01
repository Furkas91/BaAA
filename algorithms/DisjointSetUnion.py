class Node:
    def __init__(self, value, parent=None):
        self.parent = parent
        self.value = value
        self.rank = 0

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return str(self.value)

    def __hash__(self):
        return hash(self.value)

    def find(self):
        """ Находит корневую вершину множества. """

        current = self
        while current.parent is not None:
            current = current.parent
        return current


def test(first: Node, second: Node) -> bool:
    """
    Проверяет находятся ли элементы в одном множестве.

    :rtype: bool
    :type first: Node
    :type second: Node
    """

    return first.find() == second.find()


def print_test(first: Node, second: Node):
    """
    Печатает результат проверки находятся ли элементы в одном множестве.

    :type first: Node
    :type second: Node
    """
    if test(first, second):
        print(f'{first} и {second} лежат в одном множестве')
    else:
        print(f'{first} и {second} не лежат в одном множестве')


def text_test(first: Node, second: Node):
    """
    Возвращает результат проверки находятся ли элементы в одном множестве текстом.

    :type first: Node
    :type second: Node
    """
    if test(first, second):
        return 'YES'
    else:
        return 'NO'

def unite(first: Node, second: Node):
    """
    Объединяет два непересекающихся множества, определенных по элементам из них

    :type first: Node
    :type second: Node
    """
    first = first.find()
    second = second.find()
    if first.rank > second.rank:
        second.parent = first
    else:
        first.parent = second


def add_node_structure(*args):
    """
    Оборочивает любое число элементов в стуктуру Node.
    """
    return [Node(arg) for arg in args]


if __name__ == '__main__':
    a, b, c, d = Node(10), Node(20), Node(35), Node(45)
    unite(a, b)
    unite(c, d)
    print_test(a, c)
    unite(b, d)
    print_test(a, c)

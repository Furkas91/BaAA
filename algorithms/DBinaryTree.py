from binary_tree import tree


class DefaultTree(tree):

    def add_with_check(self, n) ->str:
        if self.search(n):
            return '+'
        else:
            self.addNode(n)
            return '-'

    def seacrh_next(self, n):
        result = self.add_with_check(n)
        current_node = self.root
        previous_node = current_node
        to_left = False
        while current_node:
            if current_node.n > n:
                previous_node = current_node
                current_node = current_node.left
                to_left = True
            elif current_node < n:
                previous_node = current_node
                current_node = current_node.right
                to_left = False
            else:
                if to_left:
                    return result+f" {previous_node.n}"
                else:
                    if current_node.right:
                        return result+f" {current_node.right}"
                    else:
                        return result+" -"

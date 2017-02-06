"""
def get_breadth_first_nodes(root):
    nodes = []
    stack = [root]
    while stack:
        cur_node = stack[0]
        stack = stack[1:]
        nodes.append(cur_node)
        for child in cur_node.get_children():
            stack.append(child)
    return nodes
"""
class Node():
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.wc = self.calc_wc()

    # Calculating W_c here
    def calc_wc(self):
        result = 1
        # Splitting list by every two characters
        l = [self.name[i:i + 2] for i in range(1, len(self.name), 2)]
        l.insert(0, self.name[0])
        # print(l)
        # Reversed traversing the list to calculate w
        for i, x in reversed(list(enumerate(l))):
            if len(x) <= 1:
                result *= 100
            else:
                if x[0] == 'M':
                    # l[i-1][-1] is the previous gear's index
                    result *= -gears[int(l[i - 1][-1])] / gears[int(x[-1])]
                elif x[0] == 'P':
                    continue
        return result


def calc_error(win, wout, wc):
    return abs(wout - wc) / abs(wout - win) * 100


def check_distance(gin, gout):
    return abs(gin - gout) <= 30


gears = [11, 23, 31, 47, 59, 71, 83, 97, 109, 127]


def main():
    l = []
    for i, gin in enumerate(gears):
        for j, gout in enumerate(gears[i + 1:], i + 1):
            if check_distance(gin, gout):
                name = str(i) + 'M' + str(j)
                l.append(Node(name, Node(str(i), None)))

    for i in l:
        print(i.name, i.parent.name, i.wc)

if __name__ == '__main__':
    main()

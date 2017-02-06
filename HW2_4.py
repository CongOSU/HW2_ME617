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
    l1 = []
    for i, gin in enumerate(gears):
        # for j, gout in enumerate(gears):
        for j, gout in enumerate(gears[i:], i):
            if check_distance(gin, gout):
                name = str(i) + 'M' + str(j)
                l1.append(Node(name, Node(str(i), None)))

    l2 = []
    for i, g in enumerate(l1):
        for j, gout in enumerate(gears):
            gin = gears[int(g.name[-1])]
            if check_distance(gin, gout) and j != int(g.parent.name):
                name = g.name + 'M' + str(j)
                l2.append(Node(name, g))
            if gout != gin:
                name = g.name + 'P' + str(j)
                l2.append(Node(name, g))

    l3 = []
    for i, g in enumerate(l2):
        for j, gout in enumerate(gears):
            gin = gears[int(g.name[-1])]
            if check_distance(gin, gout) and j != int(g.parent.name[-1]):
                name = g.name + 'M' + str(j)
                l3.append(Node(name, g))
            if gout != gin and g.name[-2] != 'P':
                name = g.name + 'P' + str(j)
                l3.append(Node(name, g))

    l4 = []
    for i, g in enumerate(l3):
        for j, gout in enumerate(gears):
            gin = gears[int(g.name[-1])]
            if check_distance(gin, gout) and j != int(g.parent.name[-1]):
                name = g.name + 'M' + str(j)
                l3.append(Node(name, g))
            if gout != gin and g.name[-2] != 'P':
                name = g.name + 'P' + str(j)
                l3.append(Node(name, g))

    for i in l3:
        if calc_error(100, -117, i.wc) <= 2.5:
            print("Found the smallest set of gears in group A:", i.name)
        if calc_error(100, 77, i.wc) <= 2.5:
            print("Found the smallest set of gears in group A:", i.name)
        if calc_error(100, 377, i.wc) <= 2.5:
            print("Found the smallest set of gears in group A:", i.name)
        if calc_error(100, -20, i.wc) <= 2.5:
            print("Found the smallest set of gears in group A:", i.name)
        if calc_error(100, -2345, i.wc) <= 2.5:
            print("Found the smallest set of gears in group A:", i.name)
        if calc_error(100, 2, i.wc) <= 2.5:
            print("Found the smallest set of gears in group A:", i.name)

    # for i in ll:
    #     print(i.name, i.parent.name, "{0:2.5}".format(i.wc))

if __name__ == '__main__':
    main()

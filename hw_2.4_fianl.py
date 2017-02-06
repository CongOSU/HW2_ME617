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


def create_layer(prevLayer, currLayer):
    for i, g in enumerate(prevLayer):
        for j, gout in enumerate(gears):
            gin = gears[int(g.name[-1])]
            if check_distance(gin, gout) and j != int(g.parent.name[-1]):
                name = g.name + 'M' + str(j)
                currLayer.append(Node(name, g))
            if gout != gin and g.name[-2] != 'P':
                name = g.name + 'P' + str(j)
                currLayer.append(Node(name, g))


def calc_error(win, wout, wc):
    return abs(wout - wc) / abs(wout - win) * 100


def check_distance(gin, gout):
    return abs(gin - gout) <= 30


def check_result(layers, win, wout):
    for layer in layers:
        for i, g in enumerate(layer):
            if calc_error(win, wout, g.wc) <= 2.5:
                return g.name

gears = [11, 23, 31, 47, 59, 71, 83, 97, 109, 127]


def main():
    l1 = []
    for i, gin in enumerate(gears):
        for j, gout in enumerate(gears):
            if check_distance(gin, gout):
                name = str(i) + 'M' + str(j)
                l1.append(Node(name, Node(str(i), None)))

    l2 = []
    create_layer(l1, l2)

    l3 = []
    create_layer(l2, l3)

    l4 = []
    create_layer(l3, l4)

    l5 = []
    create_layer(l4, l5)

    l6 = []
    create_layer(l5, l6)

    l7 = []
    create_layer(l6, l7)

    # l8 = []
    # create_layer(l7, l8)

    # l9 = []
    # create_layer(l8, l9)

    layers = [l1, l2, l3, l4, l5, l6,l7]

    print("The amount of sets of gears in layer 1:", len(l1))
    print("The amount of sets of gears in layer 2:", len(l2))
    print("The amount of sets of gears in layer 3:", len(l3))
    print("The amount of sets of gears in layer 4:", len(l4))
    print("The amount of sets of gears in layer 5:", len(l5))
    print("The amount of sets of gears in layer 6:", len(l6))
    print("The amount of sets of gears in layer 7:", len(l7))
    # print("The amount of sets of gears in layer 8:", len(l8))
    # print("The amount of sets of gears in layer 9:", len(l9))

    print("Found the smallest set of gears in group A:", check_result(layers, 100, -117))
    print("Found the smallest set of gears in group B:", check_result(layers, 100, 77))
    print("Found the smallest set of gears in group C:", check_result(layers, 100, 377))
    print("Found the smallest set of gears in group D:", check_result(layers, 100, -20))
    print("Found the smallest set of gears in group E:", check_result(layers, 100, -2345))
    print("Found the smallest set of gears in group F:", check_result(layers, 100, 2))

    # for i in l2:
        # print(i.name, i.parent.name, "{0:2.5}".format(i.wc))

if __name__ == '__main__':
    main()

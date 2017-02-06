class Node():
    def __init__(self, name, parent, wout):
        self.name = name
        self.parent = parent
        self.wout = wout
        self.wc = self.calc_wc()
        self.teeth = self.calc_teeth()
        self.teeth_f = self.teeth + estimateDTG(gears[int(self.name[len(self.name)-1])],self.wout,self.wc)

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
    
    def calc_teeth(self):
        result = 0
        a = ' '.join(filter(lambda x: x.isdigit(), self.name))
        l = [int(x) for x in a.split(' ')]
        for i in l:
            result += gears[i]
        return result



def create_layer(prevLayer, currLayer):
    for i, g in enumerate(prevLayer):
        for j, gout in enumerate(gears):
            gin = gears[int(g.name[-1])]
            if check_distance(gin, gout) and j != int(g.parent.name[-1]):
                name = g.name + 'M' + str(j)
                currLayer.append(Node(name, g, gout))
            if gout != gin and g.name[-2] != 'P':
                name = g.name + 'P' + str(j)
                currLayer.append(Node(name, g, gout))


def calc_error(win, wout, wc):
    return abs(wout - wc) / abs(wout - win) * 100


def check_distance(gin, gout):
    return abs(gin - gout) <= 30


def check_result(layers, win, wout):

    def getKey(Node):
        return Node.teeth_f

    lista = []
    for layer in layers:
        for i, x in enumerate(layer):
            lista.append(x)
    lista.sort(key = getKey, reverse = True)
    while not list == []:
        chex = lista.pop()
        if calc_error(win, wout, chex.wc) <= 2.5:
            return chex.name


def estimateDTG(prevteeth, wout, wc):
    estimate = (prevteeth * wout)/wc
    if estimate < 0:
        estimate = gears[0]+abs(estimate)
    return estimate

gears = [11, 23, 31, 47, 59, 71, 83, 97, 109, 127]


def main():
    l1 = []
    for i, gin in enumerate(gears):
        for j, gout in enumerate(gears[i:], i):
            if check_distance(gin, gout):
                name = str(i) + 'M' + str(j)
                l1.append(Node(name, Node(str(i), None, gout),gout))

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

    #l7 = []
    #create_layer(l6, l7)

    #l8 = []
    #reate_layer(l7, l8)

    layers = [l1, l2, l3, l4, l5, l6]#, l7, l8]

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

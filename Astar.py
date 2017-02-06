import sys

class gearbox():
    def __init__(self, wout, prevw_cin, mfgplan):
        self.wout = wout
        self.prevw_cin = prevw_cin
        self.mfgplan = mfgplan
        self.w_cout = self.calc_wc()
        self.g = self.calcg()
        self.h = self.calch()
        self.f = self.g + self.h

    def calcg(self):
        result = 0
        a = ' '.join(filter(lambda x: x.isdigit(), self.mfgplan))
        l = [int(x) for x in a.split(' ')]
        for i in l:
            result += gears[i]
        return result

    def calch(self):
        more = int(gears[int(self.mfgplan[len(self.mfgplan) - 1])]*self.w_cout)/self.wout
        if more
        return result
    def calc_wc(self):
        result = 1
        # Splitting list by every two characters
        l = [self.mfgplan[i:i + 2] for i in range(1, len(self.mfgplan), 2)]
        l.insert(0, self.mfgplan[0])
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
    return (abs(float(wout) - float(wc)) / abs(float(wout) - float(win)) * 100.00)


# All gear options (global)
gears = [11, 23, 31, 47, 59, 71, 83, 97, 109, 127]


def main():
    # Goal
    error = 2.5

    def getKey(gearbox):
        return gearbox.f

    # Problem Inputs
    w_in = 100
    w_out = [-117, 77, 377, -20, 2, -2345]

    # Loop for DFS
    for problem in range(1, 7, 1):
        treeSearch = []
        prev = []
        globalprev = []
        # create depth 1
        for i in range(0, 10, 1):
            mfge = str(i)
            treeSearch.append(gearbox(w_out[problem], w_in, mfge))
        # print i
        branchingFactor = []
        count = 0
        c = 0

        while error == 2.5:
            count = count + 1
            treeSearch.sort(key=getKey, reverse=True)
            #sorted(treeSearch, key=getKey)
            gearcheck = treeSearch.pop()
            recentg = gears[int(gearcheck.mfgplan[len(gearcheck.mfgplan) - 1])]
            if len(gearcheck.mfgplan) < 3:
                recentg2 = '0'
            else:
                recentg2 = gears[int(gearcheck.mfgplan[len(gearcheck.mfgplan) - 3])]
            globalprev.append(gearcheck.w_cout)
            # print(gearcheck.mfgplan)
            if len(gearcheck.mfgplan) < 2:
                recento = 'N'
            else:
                recento = gearcheck.mfgplan[len(gearcheck.mfgplan) - 2]
            if len(gearcheck.mfgplan) < 4:
                recento2 = 'N'
            else:
                recento2 = gearcheck.mfgplan[len(gearcheck.mfgplan) - 4]

            depth = ((len(gearcheck.mfgplan) - 1) / 2) + 1
            print(calc_error(w_in, w_out[problem - 1], gearcheck.w_cout))
            if calc_error(w_in, w_out[problem - 1], gearcheck.w_cout) <= error:
                print(calc_error(w_in, w_out[problem - 1], gearcheck.w_cout))
                print(w_in)
                print(w_out[problem - 1])
                print(gearcheck.w_cout)
                break

            # if at depth 10, do not add children
            childrenadded = 0
            if depth < 10:
                for i in range(0, 10, 1):
                    # if gear teeth are not within 30, do not add
                    if gears[i] == recentg2:
                        if recento2 == "M":
                            continue
                    if abs(gears[i] - recentg) > 30:
                        continue
                    newgear = gearbox(w_out[problem], gearcheck.w_cout, (gearcheck.mfgplan + "M" + str(i)))
                    for p in range(0, len(globalprev), 1):
                        if newgear.w_cout == globalprev[p]:
                            continue
                    treeSearch.append(newgear)
                    #print("adding M" + str(i))
                    childrenadded = childrenadded + 1

                # if previous operation was a pair, do not add paired children or if it is first two depths
                # add paired children to stack
                for i in range(0, 10, 1):
                    if recento == 'P':
                        continue
                    if depth < 2:
                        continue
                    if gears[i] == recentg:
                        continue
                    # push onto stack
                    newgear = gearbox(w_out[problem], gearcheck.w_cout, (gearcheck.mfgplan + "P" + str(i)))
                    treeSearch.append(newgear)
                    #print("adding P" + str(i))
                    childrenadded = childrenadded + 1

            # if childrenadded == 0:
            #	depth = depth - 1
            # else:
            #	depth = depth + 1
            # print(str(count) + "loop moving to depth" + str(depth))
            if not childrenadded == 0:
                c = c + 1
                branchingFactor.insert(c - 1, childrenadded)

        print("The solution for problem " + str(problem) + " is " + gearcheck.mfgplan)
        x = 0
        for n in range(0, len(branchingFactor) - 1, 1):
            x = x + branchingFactor[n]
        print("The branching factor is " + str(x / (len(branchingFactor) + 1)))


main()
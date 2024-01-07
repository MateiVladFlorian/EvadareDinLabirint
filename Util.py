import random as r


class Util:
    @staticmethod
    def Manhattan(px, py, ex, ey):
        dx = abs(px - ex)
        dy = abs(py - ey)
        return dx + dy

    @staticmethod
    def ChooseMap():
        index = r.randint(1, 5)
        path = "Maps/Labirint{}.txt".format(index)
        m = []
        map = open(path, 'r')

        for line in map:
            array = []

            for i in range(len(line.split(' '))):
                array.append(int(line.split(' ')[i]))

            m.append(array)

        map.close()
        return m

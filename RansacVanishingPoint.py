
# Define line, two points determine a line
class Line(object):

    def init(self, line):

        self.x1 = line[0]

        self.y1 = line[1]

        self.x2 = line[2]

        self.y2 = line[3]

    # calculate the parameters of the line
    def getlineparam(line):
        """
        For the line equation a*x+b*y+c=0, if we know two points(x1, y1)(x2,y2) in line, we can get
            a = y1 - y2
            b = x2 - x1
            c = x1*y2 - x2*y1
        """
        a = line.y1 - line.y2
        b = line.x2 - line.x1
        c = line.x1 * line.y2 - line.x2 * line.y1
        return a, b, c

    # calculate the intersection of the two lines
    def getcrosspoint(line1, line2):
        """
        if we have two lines: a1*x + b1*y + c1 = 0 and a2*x + b2*y + c2 = 0,
        when d(= a1 * b2 - a2 * b1) is zero, then the two lines are coincident or parallel.
        The cross point is :
            x = (b1 * c2 - b2 * c1) / d
            y = (a2 * c1 - a1 * c2) / d
        """

        a1, b1, c1 = getlineparam(line1)
        a2, b2, c2 = getlineparam(line2)
        d = a1 * b2 - a2 * b1
        if d == 0:
            return np.inf, np.inf
        x = (b1 * c2 - b2 * c1) / d
        y = (a2 * c1 - a1 * c2) / d
        return x, y

# Establish vanishing point model
# define a fitting function and a distance function

class pointModel(Model):
    def __init__(self):
        self.params = None
        self.residual = 0

    def fit(self, lines):
        lines = lines[:, 0]
        X = []
        Y = []

        for i in range(len(lines) - 1):
            line1 = Line(lines[i])
            line2 = Line(lines[i + 1])
            x, y = getcrosspoint(line1, line2)
            X.append(x)
            Y.append(y)

        X = np.asarray(x).mean()
        Y = np.asarray(y).mean()
        self.params = [X, Y]

        for i in range(len(lines)):
            line = Line(lines[i])
            a, b, c = getlineparam(line)
            self.residual += abs(a * X + b * Y + c) / np.sqrt(a * a + b * b)

    def distance(self, samplelines):
        dists = []
        for line in samplelines:
            line = Line(line[0, :])
            [x, y] = self.params
            a, b, c = getlineparam(line)
            dist = abs((a * x + b * y + c) / np.sqrt(a * a + b * b))
            dists.append(dist)
        return np.asarray(dists)

    # Ransac Al
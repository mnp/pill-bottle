class Common:

    def __init__(self, nparts):
        self.edges = {}
        self.nparts = nparts;

    def add_edge (self, w0, h0, w1, h1):
        e = ("\"%d,%d\" -> \"%d,%d\"" % (w0, h0, w1, h1))
        if e in self.edges:
            return False        # short circuit - stop descending
        else:
            self.edges[e] = 1
            return True         # new edge - keep going

    def draw_pill(self, wholes, halves):
        '''Make an edge for all states.'''
        if wholes > 0:
            new_halves =  halves + self.nparts - 1
            if self.add_edge(wholes, halves, wholes-1, new_halves):
                self.draw_pill(wholes-1, new_halves)
        if halves > 0:
            if self.add_edge(wholes, halves, wholes, halves-1):
                self.draw_pill(wholes, halves-1)

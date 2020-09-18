import mathutils

def _intersect_line2_line2(A, B):
    d = B.v.y * A.v.x - B.v.x * A.v.y
    if d == 0:
        return None

    dy = A.p.y - B.p.y
    dx = A.p.x - B.p.x
    ua = (B.v.x * dy - B.v.y * dx) / d
    if not A.intsecttest(ua):
        return None
    ub = (A.v.x * dy - A.v.y * dx) / d
    if not B.intsecttest(ub):
        return None

    return mathutils.Vector((A.p.x + ua * A.v.x, A.p.y + ua * A.v.y))

class LineSegment2:
    def __init__(self, _p1, _p2):
        self.p =  _p1
        self.p1 = _p1
        self.p2 = _p2
        self.v = _p2 - _p1

    def __repr__(self):
        return 'LineSegment2(<%.2f, %.2f> to <%.2f, %.2f>)' % \
            (self.p.x, self.p.y, self.p.x + self.v.x, self.p.y + self.v.y)

class Ray2:
    def __init__(self, _p, _v):
        self.p = _p
        self.p1 = _p
        self.p2 = _p+_v
        self.v = _v

    def __repr__(self):
        return 'Ray2(<%.2f, %.2f> + u<%.2f, %.2f>)' % \
            (self.p.x, self.p.y, self.v.x, self.v.y)

    def intsecttest(self,u):
        return u>=0.0

    def intersect(self,other):
        return _intersect_line2_line2(self,other)

class Line2:
    def __init__(self, p1, p2=None, ptype=None):
        if p2 is None: # p1 is a LineSegment2, a Line2 or a Ray2
            self.p = p1.p.copy()
            self.v = p1.v.copy()
        elif ptype == 'pp':
            self.p = p1.p.copy()
            self.v = p2-p1
        elif ptype == 'pv':
            self.p = p1.copy()
            self.v = p2.copy()
        self.p1 = self.p
        self.p2 = self.p+self.v

    def __repr__(self):
        return 'Line2(<%.2f, %.2f> + u<%.2f, %.2f>)' % \
            (self.p.x, self.p.y, self.v.x, self.v.y)

    def intsecttest(self,u):
        return True

    def intersect(self,other):
        intsect = _intersect_line2_line2(self,other)
        return intsect

    def distance(self,other): # other is a vector
        nearest = mathutils.geometry.intersect_point_line(other, self.p, self.p+self.v)[0]
        dist = (other-nearest).length
        return dist
 
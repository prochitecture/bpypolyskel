import numpy as np

def normalize(vector): # normlaize to unit vector (unfortunately does not exist in numpy)
    return vector / np.linalg.norm(vector)

# -------------------------------------------------------------------------
# from https://bryceboe.com/2006/10/23/line-segment-intersection-algorithm/,

def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])
# Return true if line segments AB and CD intersect
def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)
# -------------------------------------------------------------------------

def _intersect_line2_line2(A, B):
    d = B.v[1] * A.v[0] - B.v[0] * A.v[1]
    if d == 0:
        return None

    dy = A.p[1] - B.p[1]
    dx = A.p[0] - B.p[0]
    ua = (B.v[0] * dy - B.v[1] * dx) / d
    if not A.intsecttest(ua):
        return None
    ub = (A.v[0] * dy - A.v[1] * dx) / d
    if not B.intsecttest(ub):
        return None

    return np.array((A.p[0] + ua * A.v[0], A.p[1] + ua * A.v[1]))

class Edge2:
    def __init__(self, p1, p2, norm=None, verts=None, center=np.zeros((1,2))):  # evtl. conversion from 3D to 2D
        """
        Args:
            p1 (numpy vector | int): Index of the first edge vertex if <verts> is given or
                the vector of the first edge vertex otherwise
            p2 (numpy vector | int): Index of the second edge vertex if <verts> is given or
                the vector of the second edge vertex otherwise
            norm : Normalized edge vector
            verts (numpy array): vertices
        """
        if verts is not None:
            self.i1 = p1
            self.i2 = p2
            p1 = verts[p1]-center
            p2 = verts[p2]-center
        self.p1 = p1[:2]
        self.p2 = p2[:2]
        if norm is not None:
            self.norm = norm[:2]
        else:
            norm = self.p2-self.p1
            self.norm = norm / np.linalg.norm(norm)


    def length_squared(self):
        return np.sum(np.square(self.p2-self.p1))

class Ray2:
    def __init__(self, _p, _v):
        self.p = _p
        self.p1 = _p
        self.p2 = _p+_v
        self.v = _v

    def intsecttest(self,u):
        return u>=0.0

    def intersect(self,other):
        return _intersect_line2_line2(self,other)

class Line2:
    def __init__(self, p1, p2=None, ptype=None):
        if p2 is None: # p1 is a LineSegment2, a Line2 or a Ray2
            self.p = p1.p1.copy()
            self.v = (p1.p2-p1.p1).copy()
        elif ptype == 'pp':
            self.p = p1.p.copy()
            self.v = p2-p1
        elif ptype == 'pv':
            self.p = p1.copy()
            self.v = p2.copy()
        self.p1 = self.p
        self.p2 = self.p+self.v

    def intsecttest(self,u):
        return True

    def intersect(self,other):
        intsect = _intersect_line2_line2(self,other)
        return intsect

    def distance(self,other): # other is a point
        return np.cross(self.v,other-self.p)/np.linalg.norm(self.v)

def fitCircle3Points(points):
    N = len(points)
    # circle through three points usingg complex math, see answer in 
    # https://stackoverflow.com/questions/28910718/give-3-points-and-a-plot-circle
    x = complex(points[0,0], points[0,1])
    y = complex(points[N//2,0], points[N//2,1])
    z = complex(points[-1,0], points[-1,0])
    w = z-x
    w /= y-x
    c = (x-y)*(w-abs(w)**2)/2j/w.imag-x
    x0 = -c.real
    y0 = -c.imag
    R = abs(c+x)
    return np.array((x0,y0)), R

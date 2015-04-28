
def overlap_percentage(rect1, rect2):
    I = max(0, min(rect1.x2, rect2.x2) - max(rect1.x1, rect2.x1)) * max(0, min(rect1.y2, rect2.y2) - max(rect1.y1, rect2.y1))
    print "Overlap: ", I
    A_1 = abs(rect1.x2 - rect1.x1) * abs(rect1.y2 - rect1.y1)
    A_2 = abs(rect2.x2 - rect2.x1) * abs(rect2.y2 - rect2.y1)
    print "Area 1: ", A_1
    print "Area 2: ", A_2
    SU = A_1 + A_2 - I
    print "Area of union: ", SU
    print "% of overlap", I * 1.0 / SU
    return I * 1.0 / A_2

class Rect(object):
    def __init__(self, x1,x2,y1,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

r1 = Rect(0,20,0,20)
r2 = Rect(10,30,10,30)
r3 = Rect(10,20,10,20)
r4 = Rect(0,25,0,25)

print overlap_percentage(r4,r2)

from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        def compute_area(x, y, a, b):
            l = a - x
            h = b - y
            area = l * h
            return area

        corners = set() 

        def check_set(bl, tl, br, tr):
            if bl in corners:
                corners.remove(bl)
            else:
                corners.add(bl)
            if tl in corners:
                corners.remove(tl)
            else:
                corners.add(tl)
            if br in corners:
                corners.remove(br)
            else:
                corners.add(br)
            if tr in corners:
                corners.remove(tr)
            else:
                corners.add(tr)

        minx, miny, maxa, maxb = rectangles[0]
        total_area = 0

        for x,y,a,b in rectangles:
            minx = min(minx, x)
            miny = min(miny, y)
            maxa = max(maxa, a)
            maxb = max(maxb, b)
            total_area += compute_area(x, y, a, b) 
            check_set((x, y), (x, b), (a, y), (a, b))

        if compute_area(minx, miny, maxa, maxb) != total_area:
            return False 
        expected = {(minx, miny), (minx, maxb), (maxa, miny), (maxa, maxb)}
        if expected != corners:
            return False
        
        return True


       


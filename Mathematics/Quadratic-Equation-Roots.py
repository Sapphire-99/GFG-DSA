import math
class Solution:
	def quadraticRoots(self, a, b, c):
        # code here
        d= b*b-4*a*c
        if d<0:
            return [-1]
        sqrt=math.sqrt(d)
        r1=math.floor((-b+sqrt)/(2*a))
        r2=math.floor((-b-sqrt)/(2*a))
        if r1>=r2:
            return [r1,r2]
        else:
            return [r2,r1]




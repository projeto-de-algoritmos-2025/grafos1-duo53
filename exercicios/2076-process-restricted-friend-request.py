class UnionFind(object):
    def __init__(self,n):
        self.weights = [-1]*n
        self.parents = [i for i in range (n)]
    def find(self,a):
        while a != self.parents[a]:
            a = self.parents[a]
        return a
    def union(self,a,b):
        ap = self.find(a)
        bp = self.find(b)
        if self.weights[ap] < self.weights[bp]:
            self.weights[ap]+=self.weights[bp]
            self.parents[bp] = ap
        else:
            self.weights[bp]+=self.weights[ap]
            self.parents[ap] = bp
class Solution(object):
    def friendRequests(self, n, restrictions, requests):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :type requests: List[List[int]]
        :rtype: List[bool]
        """
        uf = UnionFind(n)
        res = []
        restrictions = set([(x,y) for x,y in restrictions])
        for i in range (len(requests)):
            p1 = uf.find(requests[i][0])
            p2 = uf.find(requests[i][1])
            p1set = set()
            p2set = set()
            for j in range (n):
                cp = uf.find(j)
                if cp == p1:
                    p1set.add(j)
                if cp == p2:
                    p2set.add(j)
            flag = True
            for x in restrictions:
                if (x[0] in p1set and x[1] in p2set) or (x[0] in p2set and x[1] in p1set):
                    flag = False
                    break
            res.append(flag)
            if flag:
                uf.union(requests[i][0],requests[i][1])
        return res
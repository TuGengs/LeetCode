# 朋友圈   (一个按顺序树的顺序查找，一个压缩路径查找，虽然快但是会导致2->0, 0-> 3情况，需要再遍历一次修正)

class Solution:

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        parent = [-1] * len(M) # parent[i] = j if i <-> j

        def find(n):
            if parent[n] == -1:
                return n
            else:
                return find(parent[n])

        def union(i, j):
            fi = find(i)
            fj = find(j)
            if fi != fj:
                parent[fi] = fj

        for pi in range(len(M)):
            for pj in range(len(M[0])):
                if M[pi][pj] == 1 and pi != pj:
                    union(pi, pj)
                    print(parent)

        count = 0
        for i in range(len(parent)):
            if parent[i] == -1:
                count += 1
        return count

    def findCircleNum2(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        father = [i for i in range(len(M))] # 可以是0，1，2，3也可以是-1 -1 -1

        def find(n):
            if father[n] != n: father[n] = find(father[n])
            return father[n]

        def union(i, j):
            father[find(j)] = find(i)

        for pi in range(len(M)):
            for pj in range(len(M[0])):
                if M[pi][pj]:
                    union(pi, pj)
                    print(father)

        for i in range(len(M)): find(i) # 2->0, 0-> 3
        return len(set(father))

if __name__ == '__main__':
    a = Solution()
    l = a.findCircleNum([[1,1,1,0,1,1,1,0,0,0],[1,1,0,0,0,0,0,1,0,0],[1,0,1,0,0,0,0,0,0,0],[0,0,0,1,1,0,0,0,1,0],[1,0,0,1,1,0,0,0,0,0],[1,0,0,0,0,1,0,0,0,0],[1,0,0,0,0,0,1,0,1,0],[0,1,0,0,0,0,0,1,0,1],[0,0,0,1,0,0,1,0,1,1],[0,0,0,0,0,0,0,1,1,1]])
    print(l)
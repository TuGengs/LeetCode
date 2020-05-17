# 岛屿数量(以前蓝桥的一道题目，怀念一下)

class Solution(object):

    # dfs消除一座岛 （快）
    def dfs(self, grid, x, y):
        grid[x][y] = 0
        nx, ny = len(grid), len(grid[0])
        for x, y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if 0 <= x < nx and 0 <= y < ny and grid[x][y] == "1":
                self.dfs(grid, x, y)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        nx = len(grid)
        if nx == 0:
            return 0
        ny = len(grid[0])

        num_islands = 0
        for x in range(nx):
            for y in range(ny):
                if grid[x][y] == "1":
                    num_islands += 1
                    self.dfs(grid, x, y)

        return num_islands

# =======================================================================
    # bfs （较快）
    def numIslands2(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        nx = len(grid)
        if nx == 0:
            return 0
        ny = len(grid[0])

        num_islands = 0

        import collections

        for x in range(nx):
            for y in range(ny):

                if grid[x][y] == "1":
                    num_islands += 1
                    deq = collections.deque([(x, y), ])
                    grid[x][y] = "0"
                    while deq:
                        tmpx, tmpy = deq.popleft()
                        # grid[tmpx][tmpy] = "0"    这样会超时,一进入队列就给0，别让算法做太多的"==1"之后的操作。
                        for xx, yy in [(tmpx - 1, tmpy), (tmpx + 1, tmpy), (tmpx, tmpy - 1), (tmpx, tmpy + 1)]:
                            if 0 <= xx < nx and 0 <= yy < ny and grid[xx][yy] == "1":
                                deq.append((xx, yy))
                                grid[xx][yy] = "0"
        return num_islands

# =======================================================================
    # 并查集 （慢）
    def numIslands3(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        class UnionFind:

            def __init__(self, n):
                self.count = n
                self.parent = [i for i in range(n)]
                self.rank = [1 for _ in range(n)]

            def get_count(self):
                return self.count

            def find(self, p):
                while p != self.parent[p]:
                    self.parent[p] = self.parent[self.parent[p]]
                    p = self.parent[p]
                return p

            def is_connected(self, p, q):
                return self.find(p) == self.find(q)

            def union(self, p, q):
                p_root = self.find(p)
                q_root = self.find(q)
                if p_root == q_root:
                    return

                if self.rank[p_root] > self.rank[q_root]:
                    self.parent[q_root] = p_root
                elif self.rank[p_root] < self.rank[q_root]:
                    self.parent[p_root] = q_root
                else:
                    self.parent[q_root] = p_root
                    self.rank[p_root] += 1

                self.count -= 1

        row = len(grid)
        # 特判
        if row == 0:
            return 0
        col = len(grid[0])

        def get_index(x, y):
            return x * col + y

        # 注意：我们不用像 DFS 和 BFS 一样，4 个方向都要尝试，只要看一看右边和下面就可以了
        directions = [(1, 0), (0, 1)]
        # 多开一个空间，把水域 "0" 都归到这个虚拟的老大上
        dummy_node = row * col

        # 多开的一个空间就是那个虚拟的空间
        uf = UnionFind(dummy_node + 1)
        for i in range(row):
            for j in range(col):
                # 如果是水域，都连到那个虚拟的空间去
                if grid[i][j] == '0':
                    uf.union(get_index(i, j), dummy_node)
                if grid[i][j] == '1':
                    # 向下向右如果都是陆地，即 "1"，就要合并一下
                    for direction in directions:
                        new_x = i + direction[0]
                        new_y = j + direction[1]
                        if new_x < row and new_y < col and grid[new_x][new_y] == '1':
                            uf.union(get_index(i, j), get_index(new_x, new_y))
        # 不要忘记把那个虚拟结点减掉
        return uf.get_count() - 1

if __name__ == '__main__':
    a = Solution()
    l = a.numIslands(None)
    print(l)
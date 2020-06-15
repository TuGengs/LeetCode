# 最多可以参加的会议数目 (最小堆)

import heapq

class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events.sort()
        start, stop = events[0][0], max(events[i][1] for i in range(len(events)))
        pq = []
        event_idx = 0
        ans = 0

        for i in range(start, stop + 1):
            while event_idx < len(events) and events[event_idx][0] == i:
                heapq.heappush(pq, events[event_idx][1])    # 加入start=当天的stop
                event_idx += 1

            if pq:
                top_event = heapq.heappop(pq)
                while pq and pq[0] == i:    # 剔除多余stop=当天的
                    heapq.heappop(pq)
                ans += 1

        return ans

if __name__ == '__main__':
    a = Solution()
    l = a.maxEvents([[1,2],[2,3],[3,4],[1,2]])
    print(l)
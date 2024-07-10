#APPROACH - 1
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)

        time = 0
        q = deque()
        while heap or q:
            time += 1
            if heap:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])

        return time

#APPROACH - 2
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_freq = max(freq.values())
        freq = list(freq.values())

        max_freq_ele = 0
        i = 0
        while i < len(freq):
            if freq[i] == max_freq:
                max_freq_ele += 1
            i += 1

        ans = (max_freq - 1) * (n+1) + max_freq_ele

        return max(ans, len(tasks))

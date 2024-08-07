class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        freq = Counter(hand)
        min_heap = list(freq.keys())
        heapq.heapify(min_heap)

        while min_heap:
            smallest = min_heap[0]
            for num in range(smallest, smallest + groupSize):
                if num not in freq:
                    return False
                freq[num] -= 1

                if freq[num] == 0:
                    if num != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)

        return True

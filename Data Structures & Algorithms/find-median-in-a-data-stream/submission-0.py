class MedianFinder:
    """
    constantly find the median and sorting 
    we using the maxHeap and the minHeap
    maxHeap keep all the smaller value and minHeap would keep all the larger value
    median = (largest (maxHeap) + smallest (minHeap)) / 2.0 (if the length is even, always making sure
    the maxHeap have more value than the minHeap)
    maxHeap: + || minHeap: -
    """
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        

    def addNum(self, num: int) -> None:
        # always push the value into the maxHeap
        heapq.heappush(self.maxHeap, -num)
        # taking the max value of the maxHeap
        val = heapq.heappop(self.maxHeap)
        # pushing it into the minHeap (keep the larger value)
        heapq.heappush(self.minHeap, -val)
        if len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
            

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
        
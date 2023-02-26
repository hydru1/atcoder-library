import random
class SimpleBinarySample():
    def __init__(self, weights):
        self.weights = weights

        n = 0
        self.weight_sums = []
        for w in self.weights:
            n += w
            self.weight_sums.append(n)

    def sample(self):
        r = random.random() * self.weight_sums[-1]

        # binary search
        left, right = 0, len(self.weight_sums)
        result = -1
        while left <= right:
            mid = (left + right) // 2

            low = 0
            if mid > 0:
                low = self.weight_sums[mid-1]
            high = self.weight_sums[mid]

            if low <= r < high:
                return mid
            elif high <= r:
                left = mid + 1
            else:
                right = mid - 1

        return result
class Solution:
    def maxArea(self, height):
        water = head = 0
        tail = len(height) - 1
        for cnt in range(tail):
            width = tail - head
            if height[head] < height[tail]:   
                res = width * height[head]
                head += 1
            else:
                res = width * height[tail]
                tail -= 1
            if res > water:
                water = res
        return water
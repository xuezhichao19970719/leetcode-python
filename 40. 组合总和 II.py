class Solution:
    def combinationSum2(self, candidates, target):
        m = [set() for i in range(target+1)]
        m[0].add(())
        candidates.sort()
        for num in candidates:
            for t in range(target, num-1, -1):
                for prev in m[t-num]:
                    m[t].add(prev + (num,))
        return list(m[-1])

from typing import List
from collections import deque
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:

        q = deque(initialBoxes)
        collected = 0
        seen = set()
        has_keys = set()
        in_hand = set(initialBoxes)

        while(q):
            cur = q.popleft()

            if status[cur] == 0 and cur not in has_keys:
                continue
            if cur in seen:
                continue

            collected += candies[cur]
            seen.add(cur)
            for k in keys[cur]:
                if k not in has_keys:
                    has_keys.add(k)
                if k in in_hand:
                    q.append(k)

            for box in containedBoxes[cur]:
                if box not in in_hand:
                    in_hand.add(box)
                    q.append(box)


        return collected 


class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]

        while stack:
            node = stack.pop()
            for i in rooms[node]:
                if not seen[i]:
                    seen[i] = True
                    stack.append(i)
        return all(seen)
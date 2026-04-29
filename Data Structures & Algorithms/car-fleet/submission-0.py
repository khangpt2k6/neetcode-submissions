class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        target = 10, position = [1,4], speed = [3, 2]
        1 -> 4 -> 7 -> 10 
        4 -> 6 -> 8 -> 10 
        target = 10, position = [4,1,0,7], speed = [2,2,1,1]
        4 -> 6 -> 8 -> 10
        1 -> 3 -> 5 -> 7 -> 9 -> 10
        -> same set 
        7 -> 8 -> 9 -> 10
        """
        cars = sorted(zip(position, speed), reverse = True)
        stack = []
        for pos, spd in cars:
            # we only append into the stack if it satisfy the condition (if stack is empty and if stack is satisfy the conditon)
            time = (target - pos) / float(spd)
            if not stack or stack[-1] < time: # a new fleet
                stack.append(time)
        return len(stack)
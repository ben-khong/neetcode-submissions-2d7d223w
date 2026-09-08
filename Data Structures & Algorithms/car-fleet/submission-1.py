"""
make a list that contains a tuple of the cars position and speed
using the first list, make another list that calculates the time it takes to reach the target rounding up

while the time of the car at the top of the stack is greater than the car behind it
    pop from the stack and set the new speed
return len of said stack
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for p, s in cars:
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)
        



            


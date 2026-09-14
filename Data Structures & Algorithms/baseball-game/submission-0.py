"""
use a stack to keep track of operations in their integer form
if +, then add the last two integers, if C, pop top, if D, multiply top by 2

return the remaining element in the stack
O(N) time and space
"""
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        not_score = "+DC"

        for op in operations:
            if op in not_score:
                if op == "+":
                    stack.append(stack[-1] + stack[-2])
                elif op == "D":
                    stack.append(stack[-1] * 2)
                else:
                    stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)
        
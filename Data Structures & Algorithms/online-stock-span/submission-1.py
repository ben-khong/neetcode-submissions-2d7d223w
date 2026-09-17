class StockSpanner:

    def __init__(self):
        self.stack = [] # [stock, span]

    def next(self, price: int) -> int:
        # if stack is empty or last price is greater than current price
        if not self.stack or self.stack[-1][0] > price:
            self.stack.append([price, 1])
        else:
            cur = [price, 1]
            # while the stack is not empty and current price is larger than the top
            while self.stack and self.stack[-1][0] <= price:
                _, span = self.stack.pop()
                cur[1] += span
            self.stack.append(cur)

        return self.stack[-1][1]



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
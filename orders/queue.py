from collections import deque

class OrderQueue:
    def __init__(self):
        self.orders = deque()

    def add_order(self, order):
        self.orders.append(order)

    def process_orders(self):
        if self.orders:
            output = ", then ".join(str(order) for order in self.orders)
            print(f"Processed {output}")
            self.orders.clear()
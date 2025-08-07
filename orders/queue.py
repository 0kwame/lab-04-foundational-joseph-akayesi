from collections import deque

class OrderQueue:
    def __init__(self):
        self.orders = deque()
        self.processed_orders = []
        self.output = ''

    def add_order(self, order):
        self.orders.append(order)

    def process_orders(self):
        while self.orders:
            order = self.orders.popleft()
            self.processed_orders.append(order)

        if self.processed_orders:
            self.output = ", then ".join(str(order) for order in self.processed_orders)
            # print(f"Processed {output}")
            # self.orders.clear()

    def undo(self):
        if self.processed_orders:
            last_order = self.processed_orders.pop()
            if self.processed_orders:
                self.output += f" → Undo {last_order} → State reverts to after processing {self.processed_orders[-1]}"
            else:
                self.output += f" → Undo {last_order} → No orders left after undo."
        else:
            self.output += " → No actions to undo."
                
    def show_output(self):
        print(f"Processed {self.output}") if self.output else print("No orders processed.")

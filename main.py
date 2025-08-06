from orders import OrderQueue


class OrderProcessingSystem:
    def __init__(self):
        self.orders = OrderQueue()

    def add_order(self, order):
        self.orders.add_order(order)

    def process_orders(self):
        self.orders.process_orders()


if __name__ == "__main__":
    system = OrderProcessingSystem()
    system.add_order(101)
    system.add_order(102)
    system.add_order(103)
    system.process_orders()
from orders import OrderQueue
from repository.products import ProductsRepository

class OrderProcessingSystem:
    def __init__(self):
        self.orders = OrderQueue()
        self.products_repository = ProductsRepository()

    def add_order(self, order):
        self.orders.add_order(order)

    def process_orders(self):
        self.orders.process_orders()
    
    def undo(self):
        self.orders.undo()


if __name__ == "__main__":
    system = OrderProcessingSystem()
    system.add_order(101)
    system.add_order(102)
    system.add_order(103)
    system.process_orders()
    system.undo()
    system.orders.show_output()
    product_1 = system.products_repository.find_product('product_1')
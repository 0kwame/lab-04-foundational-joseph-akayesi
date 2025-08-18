from orders import OrderQueue, BubbleSort
from repository.products import ProductsRepository

class OrderProcessingSystem:
    def __init__(self):
        self.queue = OrderQueue()
        self.products_repository = ProductsRepository()
        self.bubble_sort = BubbleSort()

    def add_order(self, order):
        self.queue.add_order(order)

    def process_orders(self):
        self.queue.process_orders()
    
    def undo(self):
        self.queue.undo()


if __name__ == "__main__":
    system = OrderProcessingSystem()
    system.add_order(103)
    system.add_order(104)
    system.add_order(101)
    system.add_order(102)
    # system.process_orders()
    # system.undo()
    # system.orders.show_output()
    product_1 = system.products_repository.find_product('product_1')

    sorted_orders = system.bubble_sort.sort(list(system.queue.orders))
    print(f"{list(system.queue.orders)} → {sorted_orders}: Orders sorted")

    # system.queue.sort_orders() 
    system.queue.show_output()
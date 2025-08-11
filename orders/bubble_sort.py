class BubbleSort:
    def sort(self, orders = []):
            n = len(orders)
            for i in range(n):
                for j in range(0, n-i-1):
                    if orders[j] > orders[j+1]:
                        orders[j], orders[j+1] = orders[j+1], orders[j]
            return orders